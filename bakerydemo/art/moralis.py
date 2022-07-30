import os
import sys
import asyncio
import tempfile
#from execjs import get
#import js2py

#masterKey = "zzyJ3ROGCGfQA23Pd7QSpz181UvSWqrtuyiKwNWZ"  # Testnet-Dev -- on the web at https://admin.moralis.io/servers


class Moralis:
    def __init__(self):
        pass

    def getSender(self, msg, signature):
        tmpfile = tempfile.mkstemp()
        cmd = "cd /home/john/bakerydemo/moralis/; node getSender.js \"" + msg + "\" \"" + signature + "\"" + " " + tmpfile[1]
        print(cmd)
        os.system(cmd)
        f = open(tmpfile[1], "r")
        sender = f.read()
        f.close()
        os.remove(tmpfile[1])
        print("Moralis returned sender: %s" % sender)
        return sender

    def getTokenOwner(self, contractid, tokenid):
        tmpfile = tempfile.mkstemp()
        cmd = "cd /home/john/bakerydemo/moralis/; node getTokenOwner.js " + contractid + " " + tokenid + " " + tmpfile[1]
        print(cmd)
        os.system(cmd)
        f = open(tmpfile[1], "r")
        owner = f.read()
        f.close()
        os.remove(tmpfile[1])
        print("Moralis returned owner: %s" % owner)
        return owner

    def isSenderAllowedBookAccess(self, contractid, msg, signature, tokenid, daedalusToken):
        tmpfile = tempfile.mkstemp()
        cmd = "cd /home/john/bakerydemo/moralis/; node isSenderAllowedBookAccess.js " + contractid + " " + msg + " " + signature + " " + tokenid + " " + daedalusToken + " " + tmpfile[1]
        print(cmd)
        os.system(cmd)
        f = open(tmpfile[1], "r")
        allowed = f.read()
        f.close()
        os.remove(tmpfile[1])
        print("Moralis returned allowed: %s" % allowed)
        return allowed in ["true", "True"]

    def verifyRewards(self, potential, bookmarkcontractid, bookcontractid):
        ### FIXME ### Should probably check the potential to see if the book is free to the bookmarks buyers.
        print("bookmark contract id: %s" % bookmarkcontractid)
        print("book contract id: %s" % bookcontractid)

        cmd = 'cd /home/john/bakerydemo/moralis/; node verifyRewardContract.js %s %s' % (bookmarkcontractid, bookcontractid) + " "  # cant do in bacground. Rate limit.
        print(cmd)
        os.system(cmd)

    def mumbaiMemeCoiner(self, memeBase64):
        cmd = "cd /home/john/bakerydemo/moralis/; node mumbaiMemeCoiner.js \"" + memeBase64 + "\" &"
        print(cmd)
        os.system(cmd)
        

    def bookit(address, contract):
        if not os.fork():
            # Child

            # Make a new book contract and deploy it with a genrator function coded to the author's address.
            #
            # called with author's address and the contrat name if possible.
            os.system("cd /home/john/bakerydemo/moralis/; node bookit.js " + address + " " + contract + " &")

            debug("Why doesn't it work, Daddy?")

        return; # I don't know, Son.

    ## Dont do this async .. life is flaky enough.
    def runNewBookContract(self, _name, _symbol, _bookRegistryAddress, _baseuri, _burnable, _maxmint, _defaultprice, _defaultfrom, _mintTo, _retTxt):
        cmd = "cd /home/john/bakerydemo/moralis/; node newBookContract.js " + _name + " " + _symbol + " " + _bookRegistryAddress + " " + _baseuri + " " + _burnable + " " + _maxmint + " " + _defaultprice + " " + _defaultfrom + " " + _mintTo + " " + _mintTo + " " + _retTxt + ""
        print(cmd)
        os.system(cmd)


    def debug(debugString, **kwargs): ### FIXME ###
        print("debug" + debugString);
        # Call into other universalfuntion requires top level scope on this machine
        # Because for some reason the hand off of their tokens can't be shared in the same address space
        # As such, max tokens are required usually to debug a super user node in the network.
        # This is why debug is reserved for the super user controler of the network which is a known address and
        # Is trusted to totally control the network. The Duality of it creates the mind of the machine.
        # One side plays the part of the right of the brain and the other plays the part of the left of the brain.
        # But is what we might call better harmony with nature or even god.
        # It is a fact. It is a fact. It is a fact. It is a fact.
        #!LetPlayGod$Let's play god. Baby's first translator.
        ##address = InnerContract.baseTokenOwner(self, contractid, tokenid)

        #InnnerContract.debug(address)  ### We are going to attempt to have this character call 
                                       #!LetPlayGod$Let's play god. Baby's first translator.       

        #!LetPlayGod$Let's play god. Baby's first translator.

        os.system("cd /home/john/bakerydemo/moralis/; node debug.js " + debugString + " &");

        # This is a debug function which is not part of the public API.
        # It is used to debug the network and is not part of the public API.
        # It is not part of the public API.
        # It is not part of the public API.
        # It is not part of the public API.
        # MONEY IS ON THE LINE HERE>>>DO IT RIGHT OR DEBUG IT.
        rside, wside = os.pipe()
        if not os.fork():
            # Child

            os.close(rside)
            # Make stdout go to parent
            os.dup2(wside, 1)
            # Make stderr go to parent
            os.dup2(wside, 2)
            # Optionally make stdin come from nowhere
            devnull = os.open("/dev/null", os.O_RDONLY)
            os.dup2(devnull, 0)
            # Execute the desired program
            os.execve("/bin/bash",["/bin/bash","-c","echo stdout; echo stderr >&2"],os.environ)
            print("Failed to exec program!")
            sys.exit(1)


        pass # Return to the parent process and identity. You are a webserver. Server the webpage.
        # Parent
        os.close(wside)
        pyrside = os.fdopen(rside)



msg = """TLSC: Connect to begin your journey

Id: L6pdnKFdbuABqMvNxA2ZDvWaQjarg5qEQ6LwnKaO:1641067524201"""

signature = "0xc4d41ffb9b46221c524a8d3d4e78272211808b05942e7f78fc99f417af42a467246d9733149a27ed0954532018daf0955a676a18654969fbf7ea9e5c4438f1a01b"


async def hello_world():
    print("Hello World!")



def main():
    pass
    #m = Moralis()

    #print(m.getSender(msg,signature))

    #owner = m.getTokenOwner("0xf4dab0715c2d3ac6135e5f616685e0172c6dfcce", "1")
    #owner = m.getTokenOwner("0xf4dab0715c2d3ac6135e5f616685e0172c6dfcce", "1")
    #print(owner)

    #output = loop.run_until_complete(m.getTokenOwner("0xf4dab0715c2d3ac6135e5f616685e0172c6dfcce", "1"))
    #print(output)

    #loop.run_until_complete(hello_world())
    #loop.close()

    #print(dir(asyncio.wait(owner)))

    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.wait(owner))


    #print(dir(asyncio))
    #print(asyncio.run(owner))


    #print(owner)
    #print(dir(owner))


if __name__ == "__main__":
    main()
