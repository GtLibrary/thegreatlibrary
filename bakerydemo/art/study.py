# This module is for studying the JRREDITOR html output ad
# generating the current artwork given the token id.
#
# Copied from the AStudyInScarlet project

import os
import sys
import time
import gzip

AVG_WORD_LENGTH = 5.8
FAILSAFE = AVG_WORD_LENGTH * 14665
START = 0x66
STARTED = 0x56
NOTSTARTED = 0x99
MAGIC = 183 # This is a hack to remove the <title> tag from the choicetext.

class Study:
    def __init__(self, filename, residual, serial, rootdir):
        self.filename = filename
        self.residual = int(residual)
        self.serial = int(serial)
        self.rootdir = rootdir


    def main(self, stoppoint, titlelen = 4):

        outstring = []
        outstring.append("<!-- Loading html file: " + self.filename + "...\n -->")
        htmlfile = open (self.rootdir + self.filename, "rb")

        #outstring.append(htmlfile.read(MAGIC + titlelen).decode("utf8", errors="ignore"))

        # Choicetext is those that the caller wants returned from the file
        choicetext = []


        tokencount = 0
        textcount = 0
        spancount = 0
        intag = False
        starttextmagic = NOTSTARTED
        entitymagic = NOTSTARTED

        byte = htmlfile.read(1)
        while byte:
            char = ''

            if byte == b'<':
                if starttextmagic == STARTED:
                    char = "</span><"
                    starttextmagic = NOTSTARTED
                else:
                    char = '<'
    
                tokencount += 1
                intag = True

            elif byte == b'>':
                char = '>'
                tokencount += 1
                intag = False
                starttextmagic = START
    
            else:  # The byte/char is a non <> char. 
                tokencount += 1
                if intag == False:

                    if byte == b'&':
                        entitymagic = STARTED

                    if entitymagic == STARTED:
                        if byte == b';':
                            entitymagic = NOTSTARTED


                        if textcount < stoppoint: # or textcount > FAILSAFE:   # We are done emiting text into the html file..
                            char = byte.decode("utf-8", 'ignore')
                            outstring.append(char)
                            textcount += 1
                            #print(char + str(textcount))
                            #print(stoppoint)

                        byte = htmlfile.read(1)
                        continue


                    # We are inside the body of the html text
                    textcount += 1

                    serial = int(textcount / self.residual)
                    remainder = textcount % self.residual

                    #if textcount > stoppoint - residual and textcount <= stoppoint:

                    if textcount > stoppoint and textcount < stoppoint + self.residual:
                        choicetext.append(byte.decode("utf-8", 'ignore'))
                        #print(byte.decode("utf-8", 'ignore'), textcount, stoppoint, self.residual)
                        #print(" T# S# R#: " + char + " " + str(textcount) + " " + str(serial) + " " + str(remainder))
                    else:
                        pass # We pass on this token because it is not "choice" enough.


                    if textcount > stoppoint: # or textcount > FAILSAFE:   # We are done emiting text into the html file..
                        #print(" T# >S# R#: " + char + " " + str(textcount) + " " + str(self.residual) + " " + str(remainder))
                        char = ""
                    else:
                        if starttextmagic == START: # We are starting to emit text into the html file
                            char = "<span id=sp." + str(spancount) +  " {{ serial." + str(serial) +" }}>" + byte.decode("utf-8", 'ignore')
                            starttextmagic = STARTED
                            spancount += 1
                        else: # We are inside the body of the test and we are not in a tag
                            char = byte.decode("utf-8", 'ignore')

                        if remainder == 0:
                            char = char + "</span><span id=sp." + str(spancount) +  " {{ serial." + str(serial) + " }}>"
                            spancount += 1
                        else:
                            pass
                else: # We are inside a tag, leave it alone.
                    char = byte.decode("utf-8", 'ignore')
        


            #sys.stdout.buffer.write(byte)
            if byte:
                outstring.append(char)


            byte = htmlfile.read(1)


        outstring.append("\n\n<!-- " + str(tokencount) + " tokens  -->")
        outstring.append("<!-- " + str(textcount) + " text tokens -->")
        if textcount == 0:
            return "nothing here but a beta bug in JRREditor txtct-" + str(textcount)

        outstring.append("<!-- " + str(stoppoint) + " is " + str(int(stoppoint/textcount*100)) + "% of the way done. -->")

        #print(choicetext)

        return ("".join(outstring).replace("<JRRE-NBSP>", "&nbsp;"), "".join(choicetext), textcount)


    def makenft(self, choicetext, outstring, serial):
        nftdir = self.rootdir + self.filename + ".nft"
        if os.path.exists(nftdir):
            #print("Directory " + nftdir + " already exists.  Skipping.")
            pass
        else:
            os.mkdir(nftdir)
            print("Created directory " + nftdir)

        
        htmlfile = gzip.open(nftdir + "/index.html."+ str(serial), "wb")
        htmlfile.write(outstring.encode())
        htmlfile.close()

        print("nftdir: " + nftdir)
        print(outstring.encode())

        nftfile = open(nftdir + "/choicetext."+ str(serial), "w")
        nftfile.write(choicetext)
        nftfile.close()

        
    def makeart(self, serial):
        stoppoint = serial * self.residual
        outstring, choicetext, textcount = self.main(stoppoint)

        self.makenft(choicetext, outstring, serial)
        

    def doresidual(self):
        stoppoint = 0
        outstring, choicetext, textcount = self.main(stoppoint, self.residual)
        #print(outstring)
        print(textcount)

        nftcount = int(textcount/self.residual)

        for i in range(nftcount+1):
            stoppoint += self.residual
            outstring, choicetext, textcount = self.main(stoppoint)
            if i % 10 == 0:
                print(str(i) + " of " + str(nftcount) + " is " + str(100*(i)/nftcount) + "%") 

            self.makenft(choicetext, outstring, i);


