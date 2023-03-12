import os   #### REPLACE WITH DB CALLSSS!!!!
import re
import gzip
import json
import base64
import shutil
import pickle
from os.path import exists
import requests
import urllib
from urllib.parse import parse_qs
import openai
import jsonlines
import random
import string

import subprocess

#print(dir(openai))


from rest_framework.response import Response
from rest_framework.decorators import api_view

from filelock import Timeout, FileLock

from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.http import JsonResponse
from django.shortcuts import redirect

from django.template import Context, Template

from bakerydemo.breads.models import BreadPage
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe

from requests_toolbelt.multipart import decoder

import bakerydemo.breads.models as books
from bakerydemo.art.study import Study
from bakerydemo.art.minter import MyFirstMinter
from bakerydemo.art.minter import MySecondMinter
#from bakerydemo.art.minter import Minter

from ebooklib import epub

from bakerydemo.art.moralis import Moralis

moralis = Moralis()

#os.environ['DJANGO_SETTINGS_MODULE']
openai.api_key = os.environ['OPENAI_API_KEY']

securePort = os.environ['securePort']
secureHost = os.environ['secureHost']
cCAPrivateKey = os.environ['cCAPrivateKey']

marketPlaceAddress = os.environ['marketPlaceAddress']
if not marketPlaceAddress:
    #marketPlaceAddress = "0x0000000000000000000000000000000000000000"
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")
    print("I dont have a marketPlaceAddress")

moralisdir = "/home/john/bakerydemo/moralis/"




def serialtest(request):

    whatafrank = "asdasd"
    serial = ["moodle"] * 400

    serial[0] = "title='serial is 0'"
    serial[1] = "title='serial is 1 now'"
    serial[2] = "title='serial is 2 now'"

    for i in range(300):
        serial[i+2] =  "title='serial is " + str(i+2) + " now'"

    context = {
        'serial': serial,
        'whatafrank': whatafrank,
    }   
    return _render(request, 'art/serialtest.html', context)


def get_serials(curserial_num, potential = None):

    my_curserial_num = 100000
    if int(curserial_num) > 100000:
        print("get_serials says::: whoa hold on. We only go to 100000?") # 100,000 why? The loop below will go nutz
    else:
        my_curserial_num = int(curserial_num)

    serial = []
    for i in range(int(my_curserial_num)):
        #print("get_serials says::: i: " + str(i))
        serial.append(' class=ss title=' + str(i) + ' name=serial.' + str(i)  + ' onmouseover=s(this)')

    context = {
        'serial': serial,
        'curserial_num': my_curserial_num,
        'potential': json.dumps(potential.__dict__, default=lambda o: 'coded'),
    }   
    return context

# FIXME: Theese are a hack, need to make the art/ directory somehow know about the datamines
# and the network.
#
# TODO: Make configuration file for the art directory/app
def getartdataminedir(datamine):
    return "/mnt/media_dir/" + datamine + "/" + datamine + ".nft/"

def getSiteName():
    return "greatlibrary.io"


def gethead(self, datamine, cur_serial):


    head = """

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="/static/css/hexagons.css">

    <script>const datamine = '""" + datamine + """';</script>
    <script>const cur_serial = '""" + str(cur_serial) + """';</script>

    <script src="https://unpkg.com/react@17/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js" crossorigin></script>


    <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
    <script src="https://unpkg.com/moralis-v1/dist/moralis.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <style>
        .modal-content iframe{ margin: 0 auto; display: block; }
    </style>

    """

    return head



def generate_bookcontractid(self, datamine):
    dataminedir = books.datamine_path(datamine)
    whoFile = dataminedir + "/contractBT" + datamine + ".txt"
    print("whoFile: " + whoFile)
    if not os.path.exists(whoFile):
        minter = Minter(self, datamine, "BT", whoFile)
        return;
    else:
        f = open(whoFile, 'r')
        contractBM = f.read().strip()
        f.close()
        return contractBM

    return False

    #minter = MyFirstMinter(potential, datamine)
    #return minter.deployBookContract()

def generate_bookmarkcontractid(self, datamine):
    dataminedir = books.datamine_path(datamine)
    whoFile = dataminedir + "/contractBM" + datamine + ".txt"
    print("whoFile: " + whoFile)
    if not os.path.exists(whoFile):
        minter = Minter(self, datamine, "BM", whoFile)
        return;
    else:
        f = open(whoFile, 'r')
        contractBM = f.read().strip()
        f.close()
        return contractBM

    return False

    #minter = MyFirstMinter(self, datamine)
    #minter.deployBookmarkContract()


def getbookmarkcontractid(self, datamine):
    dataminedir = books.datamine_path(datamine)
    try:
        f = open(dataminedir + "/contractBM" + datamine + ".txt", "r")
        contractid = f.read().strip()
        return contractid.strip().lower()
    except:
        generate_bookmarkcontractid(self, datamine)
        f = open(dataminedir + "/contractBM" + datamine + ".txt", "r")
        contractid = f.read().strip()
        return contractid.strip().lower()
    return "unknowncontractid-GAMMA"


def getbookcontractid(potential, datamine):
    dataminedir = books.datamine_path(datamine)

    try:
        f = open(dataminedir + "/contractBT" + datamine + ".txt", "r")
        bookcontractid = f.read().strip()
        f.close()
        return bookcontractid.lower();
    except:
        generate_bookcontractid(potential, datamine)
        f = open(dataminedir + "/contractBT" + datamine + ".txt", "r")
        bookcontractid = f.read().strip()
        f.close()
        return bookcontractid.lower()

    return "unknowncontractid-ALPHA"

def verifyRewards(potential, datamine, bookmarkcontractid, bookcontractid):
    print("verifyRewards: " + str(bookmarkcontractid) + " " + str(bookcontractid))
    verified = getFromBackend(getbookmarkcontractid(potential, datamine) + "/verifyrewards/" + getbookcontractid(potential, datamine)) 
    return verified


def Minter(potential, datamine, contractType, whoFile):
    #Minter(self, datamine, "HB", whoFile)

    #self.potential = potential
    _datamine = datamine
    _name = contractType + potential._name
    _symbol = contractType + potential._symbol
    _bookRegistryAddress = potential._bookRegistryAddress
    _baseuri = potential._baseuri
    _burnable = potential._burnable
    _maxmint = potential._maxmint
    _defaultprice = potential._defaultprice
    _defaultfrom = potential._defaultfrom
    _mintTo = potential._mintTo

    #return moralis.runNewBookContract(_name, _symbol, _bookRegistryAddress, _baseuri, _burnable, _maxmint, _defaultprice, _defaultfrom, _mintTo, who) ##, unknown // moralis got it.

    secureUri = "0x0" + "/newbookcontract/" + _name + "/" + _symbol+ "/" + _bookRegistryAddress + "!" + _baseuri + "!"
    secureUri += _burnable + "/" + _maxmint + "/" + _defaultprice + "/" + _defaultfrom + "/" + _mintTo + "!" + whoFile

    print(secureUri)
    contractid = getFromBackend(secureUri)
    print("contract on python side: " + contractid)
    f = open(whoFile, "w")
    f.write(contractid)
    f.close()



fifoWrite = 0 # Zero means no fd
def getFifoWrite():
    writeFifo = os.environ["ALPHA_FIFO"]
    global fifoWrite
    if fifoWrite == 0:
        fifoWrite = os.open(writeFifo, os.O_WRONLY)
    return fifoWrite

def getFromBackend(url):

    print("cCAPrivateKey: " + cCAPrivateKey)

    if cCAPrivateKey != "encrypted":
        print("getFromBackend: " + url)
        tmpFile = os.environ["SERVICE_TMPFILE"]
        print("tmpFile: " + tmpFile)
        f = open(tmpFile, 'r')
        port = f.read().strip()
        print("port: " + str(port))
        f.close()

        response = requests.get("http://localhost:" + port + "/" + url)
        print("response: " + response.text)
        return response.text
    else:
        print("secure request incoming")
        port = securePort
        host = secureHost

        response = requests.get("https://" + host + ":" + port + "/" + url, verify="/home/john/bakerydemo/moralis/cert.pem")
        print("response: " + response.text)
        return response.text

def getBookmarkTotalSupply(potential, datamine):
    print("getBookmarkTotalSupply: " + str(datamine))

    currentBookmarlTotalSupply = getFromBackend(getbookmarkcontractid(potential, datamine) + "/totalsupply")
    print("currentBookmarlTotalSupply: " + str(currentBookmarlTotalSupply))
    try:
        currentBookmarlTotalSupply = int(currentBookmarlTotalSupply)
        return int(currentBookmarlTotalSupply)
    except:
        print("error: " + str(currentBookmarlTotalSupply))


def getTotalBMTokens(potential, datamine):
    print("In getTotalBMTokens")
    dataminedir = books.datamine_path(potential.datamine)

    return getBookmarkTotalSupply(potential, datamine)  # this should ensure the .totalsupply file exists if possible

def generate_hardboundcontractid(self, datamine):
    dataminedir = books.datamine_path(datamine)
    whoFile = dataminedir + "/contractHB" + datamine + ".txt"
    print("whoFile: " + whoFile)
    if not os.path.exists(whoFile):
        minter = Minter(self, datamine, "HB", whoFile)
        return;
    else:
        f = open(whoFile, 'r')
        contractBM = f.read().strip()
        f.close()
        return contractBM

    return False

    #minter = MyFirstMinter(potential, datamine)
    #return minter.deployHardboundContract()

def gethardboundcontractid(potential, datamine):
    dataminedir = books.datamine_path(potential.datamine)

    try:
        f = open(dataminedir + "/contractHB" + potential.datamine + ".txt", "r")
        contractid = f.read().strip()
        f.close()
        return contractid.strip().lower()
    except:
        generate_hardboundcontractid(potential, datamine)
        f = open(dataminedir + "/contractHB" + potential.datamine + ".txt", "r")    
        contractid = f.read().strip()
        f.close()
        return contractid.strip().lower()

    return "HB-ALPHA-CONTRACTID"




def getaccount(potential, datamine):
    pass

def loadSite():
    rawjs = """</script><script>"""
    for sitefile in ["defaults.js", "books.nft.js", "moralisweb3.js"]:     # This is the include order.... careful
        f = open("/home/john/bakerydemo/bakerydemo/static/js/" + sitefile, "r") 
        rawjs += f.read() + """</script><script>"""
    return rawjs;

def getbody(potential, datamine):

    #account = getaccount(potential, datamine)


    bookmarkcontractid = getbookmarkcontractid(potential, datamine)
    bookcontractid = getbookcontractid(potential, datamine)
    hardboundcontractid = gethardboundcontractid(potential, datamine)

    #### Make sure that the book contract is set as the bookmark's reward contract
    verifyRewards(potential, datamine, bookmarkcontractid, bookcontractid)
    getBookmarkTotalSupply(potential, datamine)

    print("generating body...")

    body = """

<div class="container" >
<div class="modal fade" id="myModal" role="dialog" style="display:none;">
<div class="modal-dialog modal-lg">
<div class="modal-content">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal">&times;</button>
<h4 class="modal-title">Inspecting Bookmark</h4>
</div>
<div class="modal-body">
    <div id="videoContainer"></div>
      <div class="mypricedongle">
      <h5>Price for bookmark: <span id="tokenspan"></span> """ + datamine + """ </h5>
       <span>Contract:</span> <span id="contractspan">BETA</span>
       <span>Network:</span><span id=networkspan>""" + getSiteName() + """</span> 
       <span>Price: </span><span id="pricespan">Caculating...</span>
       <span id="offeringspantext" style="display:none;">Offering: </span><span id="offeringspan" style="display:none;">Finding...</span>

       <button type="button" id="btn-buy-bmrk" onclick=buythisbookmark(event)>Buy bookmark</button>
       <button type="button" id="btn-pet-ben" onclick=petben(event)>Pet BEN</button>

       <hr>

       <h5>For owner <span id="ownerspan">unknown</span></h5>
       <button type="button" id="btn-sell-bmrk" onclick=sellthisbookmark(event)>Sell bookmark</button>
       for: <input type="text" id="sellerprice" name="fname" value="5"><br>
       <button type="button" id="btn-send-bmrk" onclick=sendthisbookmark(event)>Send bookmark</button>
       to: <input type="text" id="toaddress" name="fname" value="0x213E6E4167C0262d8115A8AF2716C6C88a6905FD" size="42"><br>

       <br>

       <hr>
         <h5>Use the Great Library's faucets directly...</h5>
         <button type="button" id="btn-test-faucet" onclick=testlibraryfaucet(event)>Request a new Culture Coin Seedling</button>

         <button type="button" id="btn-test-bmrk" onclick=testthisbookmark(event)>Test bookmark</button>
         <input type="text" id="testprice" name="fname" value="Hi BEN!"><br><br>
         <pre id="testresult"></pre>

      <hr>
         <h5>The Great Library's Bridge</h5>
         <button type="button" id="btn-apply-rates" onclick=applydexrates(event)>Apply DEX rates</button>
         X Rate: <input type="text" id="dexXMTSPRateId" size="5" value=""> CC Rate: <input type="text" id="dexCCRateId" size="5" value=""><br><br>
         <button type="button" id="btn-find-rates" onclick=finddexrates(event)>Find new DEX rates</button>
         <hr>
         <button type="button" id="btn-set-stake-rate" onclick=setstakerate(event)>Set Stake Rate</button>
         Stake Rate: <input type="text" id="stakerateid" size="5" value="">
         <button type="button" id="btn-get-stake-rate" onclick=getstakerate(event)>Get Stake Rate</button>


      </div>

 
</div>
<div class="modal-footer">
<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
</div>
</div>
</div>
</div>
</div>


    <div id="app-header-btns"></div>
    <section id="content" class="container"></section>
    <!-- script>  + loadSite()  + </script -->
    <script src="/static/js/defaults.js"></script>
    <script src="/static/js/moralisweb3.js"></script>
    <script src="/static/js/books.nft.js"></script>

    <style>
.box{
    display: none;
    width: 100%;
}

span:hover + .box,.box:hover{
    display: inline;
    position: relative;
    z-index: 100;
}
    </style>

        <main> <!-- Marketplace -->
            <div class="container mt-5" id="bookDiv">
                <div class="row">
                    <h4 id="balance" ></h4>
                </div>
                <div class="row">
                    <div class="col-lg-6">
                        <div class="text-center bg-dark text-white">

                        </div>
                        <div id="offeringList" class="text-center">
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="text-center bg-dark text-white">
                        </div>
                        <div id="featured_nft"class="text-center">
                        </div>
                    </div>
                </div>
            </div>
        </main>

    <script>
    //var datamine = '""" + datamine + """'; // Set earlier in head. --jrr
    var bookmarkcontractid = '""" + bookmarkcontractid + """';
    var bookcontractid = '""" + bookcontractid + """';
    var hardboundcontractid = '""" + hardboundcontractid + """';
    var potential = '{{ potential }}';

    var serial_num = 0;
    var curid = "sp.0";


    function s(ref) {

        curid = ref.id;
        console.log(ref); 
        var cur_serial = ref.getAttribute("name").split('.')[1];
        serial_num = cur_serial;

        return books_nft_handoff(ref, datamine, bookmarkcontractid, "The Great Library", serial_num);


        ref.title = "Bookmark: " + serial_num + ", ContactID: " + bookmarkcontractid;
        console.log("Bookmark: " + serial_num + ", ContactID: " + bookmarkcontractid);

        ref.onmouseover = function(e) {
            var cur_serial = ref.getAttribute("name").split('.')[1];
            serial_num = cur_serial;
            console.log("Mouse over: " + ref.id);
            curid = ref.id;
        };

        html = '<span></span>';


        emb = document.createElement("div");
        emb.innerHTML = html;

        insertAfter(ref, emb.firstChild);


    }

    </script>

    """

    print ("body generated")

    return body


def recodehtml(self, html, datamine="TLSC", cur_serial=0):
   html = html.decode('utf-8', errors="ignore")

 
   html = html.replace('<head>', '<head>' + gethead(self, datamine, cur_serial))
   html = html.replace('</head>', '</head>')

   html = html.replace('<body>', '<body style="margin:10px;padding:0>' + getbody(self, datamine))
   html = html.replace('</body>', '</body>')

   html = html.replace('.jpeg', '.jpeg?datamine=' + datamine)
   html = html.replace('.jpg', '.jpg?datamine=' + datamine)
   html = html.replace('.png', '.png?datamine=' + datamine)
   html = html.replace('style.css', 'style.css?datamine=' + datamine)

   return html.encode('utf-8')


#
# Calulate the portential of the contract/work of art.
#
class Potential():

    def __init__(self, datamine, curserial_num, arttype, error_fingerprint):
        self.warning = "BETA! This is a work in progress.  Please report any bugs to the author: johnrraymond@yahoo.com."
        self.datamine = datamine
        self.curserial_num = curserial_num
        self.error_fingerprint = error_fingerprint

        self.page = BreadPage.objects.filter(datamine=self.datamine)

        self.arttype = arttype
        self.title = self.get_title()
        self.books = self.get_books()
        self.bookmarks = self.get_bookmarks()
        self.cost = self.get_cost()
        self.net = self.get_net()
        self.booksales = self.get_booksales()
        self.bookmark_sales = self.get_bookmarksales()
        self.sales = self.get_total_sales()

        self.startingpoint = self.page[0].startpoint
        self.bookmarkprice = self.page[0].bookmarkprice
        self.bookprice = self.page[0].bookprice
        self.maxbooksupply = self.page[0].maxbooksupply
        self.maxbookmarksupply = self.page[0].maxbookmarksupply

        self.hardbound = self.page[0].hardbound
        self.hardboundprice = self.page[0].hardboundprice
        self.hardboundfrom = self.page[0].hardboundfrom

        self.authorwallet = self.page[0].authorwallet

        potential_name = datamine
        potential_symbol = datamine
        potential_bookRegistryAddress = marketPlaceAddress
        potential_baseuri = "https://greatlibrary.io/nft/"
        potential_burnable = "true"
        potential_maxmint = self.maxbookmarksupply
        potential_defaultprice = self.bookmarkprice;
        potential_defaultfrom = self.startingpoint;
        potential_mintTo = self.authorwallet;
        #potential_whoFilePath = getWhoFilePath(self.datamine)coin

        print("potential_mintTo: " + potential_mintTo)

        self._name = potential_name
        self._symbol = potential_symbol
        self._bookRegistryAddress = potential_bookRegistryAddress
        self._baseuri = potential_baseuri
        self._burnable = potential_burnable
        self._maxmint = potential_maxmint
        self._defaultprice = potential_defaultprice
        self._defaultfrom = potential_defaultfrom
        self._mintTo = potential_mintTo
        #self._whoFilePath = potential_whoFilePath


    def get_bookprice(self):
        try:
            return int(self.page[0].bookprice)
        except:
            self.warning = self.warning + "Using an average book price. "
            return 6

    def get_bookmarks(self):
        try:
            return int(self.page[0].maxbookmarksupply)
        except:
            self.warning = self.warning + "No maxbookmarksupply. "
            return 22222

    def get_books(self):
        try:
            return int(self.page[0].maxbooksupply)
        except:
            self.warning = self.warning + "No maxbooksupply. "
            return 100000

    def get_title(self):

        if len(self.page) == 0:
            return "Project is not in the database? ERROR code: SANITY CHECK: " + self.datamine

        return self.page[0].title
        

    def get_error_fingerprint(self):
        return self.error_fingerprint

    def get_datamine(self):
        return self.datamine

    def get_curserial_num(self):
        return self.curserial_num

    def get_work(self):
        if self.books == -1:
            self.warning = self.warning + "Using average work of ~130,000 tokens per book including bookmarks. "
            return 22222 + 100000       # Average Bookmarks + books

        return self.books + self.bookmarks

    def get_booksales(self):
        if self.books == -1:
            return 22222 * self.get_bookprice()           # Average Books * book price.

        return self.books * self.get_bookprice()      # Books * book price.

    def get_bookmarkprice(self):
        return 0                    # TODO: Get this from the database. 6 CB is the default price for a book/mark.
                                    # Effectively, 0 as long as the book is free at the same time as buying the bookmark.

    def get_bookmarksales(self):
        if self.books != -1:
            return 22222 * self.get_bookmarkprice()       # Average Bookmarks * book price.

        return self.bookmarks * self.get_bookmarkprice()      # Bookmarks * book price.

    def get_total_sales(self):
        total_sales = 0
        total_sales += self.get_booksales() 
        total_sales += self.get_bookmarksales()
        return total_sales

    def get_cost(self):
        cost = 350                      # Base cost of 350 Cultural Bits. For cover and bookmark art
        cost += 0.1 * self.get_work() # 0.1 CBs per unit of work.

        return cost

    def get_net(self):
        cost = self.get_cost() 
        roi = self.get_total_sales()
        net = roi - cost

        return net


def calculate_project_potential(datamine, curserial_num, arttype, returntype="object", error_fingerprint="SUCCESS"):
    potential = Potential(datamine, curserial_num, arttype, error_fingerprint)

    if returntype == "json":
        return json.dumps(potential.__dict__, default=lambda o: 'coded')

    return potential




def jrreditor_get_current_html(potential, cur_serial):
    dataminedir = books.datamine_path(potential.datamine)
    indexfile = books.datamine_get_index(potential.datamine)
    bookmarkfile = books.datamine_get_bookmark(potential.datamine)


    bytesperbookmark = int(potential.page[0].bperbookmark)
    #try:
    #   btyesperbookmark = int(potential.page[0].bperbookmark)
    #   study.doresidual("jrre-index.html", cur_serial, bytesperbookmark, dataminedir )
    #except:
    #   pass

    # Precode the html. This might get ugly and slower.. move to save function.
    #
    #f = open(indexfile, "r")
    #html = f.read()
    #html.replace("&nbsp;", "<JRRE-NBSP>")
    #f.close()
    #f = open(indexfile, "w")
    ##f.write(html)
    #f.close()


    study = Study("jrre-index.html", bytesperbookmark, cur_serial, dataminedir + "/")
    study.makeart(int(cur_serial))


    # Decode the html.
    #f = open(indexfile, "r")
    #html = f.read();
    #html.replace("<JRRE-NBSP>", "&nbsp;")
    #f.close()
    #f = open(indexfile, "w")
    #f.write(html)
    #f.close()


    return "study done" + str(cur_serial)


def getmagiccachefile(datamine, curserial_num, arttype):
    dataminedir = books.datamine_path(datamine)

    cachefile = dataminedir + "/CACHE-" + str(curserial_num) + "-" + arttype + ".pickle"
    return cachefile


def jrreditor_get_art_html(potential, cur_serial, arttype):

    if(potential.page[0].curserial_number < cur_serial):
        potential.warning = potential.warning + "The current serial number is higher than the serial number in the database. "
        #throw("The current serial number is higher than the serial number in the database.")

    html = jrreditor_get_current_html(potential, cur_serial);

    return html


def ownTheToken(potential, datamine, msg, signature, tokenid, daedalusToken=0):
        sender = moralis.getSender(msg, signature)
        print("sender: " + sender)

        contractid = getbookcontractid(potential, datamine)
        print("contractid: " + contractid)

        #tokenOwner = moralis.getTokenOwner(contractid, tokenid)
        #print(tokenOwner)
        #print("tokenOwner: " + tokenOwner)

        if moralis.isSenderAllowedBookAccess(contractid, msg, signature, tokenid, daedalusToken):
            potential.canAccessBook = True
            return True
        else:
            potential.canAccessBook = False
            return False

        potential.canAccessBook = False
        return False


def myredirect(request, url):
    download = request.GET.get('download', None)

    if None == download:
        pass
    else:
        url = url + "&download=" + download

    print("redirecting to: " + url)

    return redirect(url);

def _render(request, artname, content): 
    download = request.GET.get('download', None)

    if None == download: 
        print("Rendering HTML")
        return render(request, artname, content)

    print("Rendering FORK")
    myRenderOut = render(request, artname, content)
    print(dir(myRenderOut))
    myRenderOut["Content-Type"] = "application/fork"
    return myRenderOut

# Create your views here.
def art(request):
    arttype = request.GET.get('type', 'book')
    curserial_num = request.GET.get('curserial_num', '')
    curserial_num = re.sub(r'[^a-zA-Z0-9\.]', '', curserial_num)
    datamine = request.GET.get('datamine', 'TLSC')
    datamine = re.sub(r'[^a-zA-Z0-9\.]', '', datamine)
    redirectCount = request.GET.get('redirect', '0')
    redirectCount = int(redirectCount)

    daedalusToken = request.GET.get('daedalusToken', '0')
    daedalusToken = re.sub(r'[^a-zA-Z0-9\.]', '', daedalusToken)

    #msg = base64.b64decode(request.GET.get('msg', '')).decode('utf-8')
    msg = request.GET.get('msg', '')
    signature = request.GET.get('sig', 'default')
    tokenid = request.GET.get('tokenid', 'default')
    print("tokenid: " + tokenid)

    potential = calculate_project_potential(datamine, curserial_num, "book", error_fingerprint="default")
    if not os.path.exists(books.datamine_path(datamine)):
        os.mkdir(books.datamine_path(datamine))

    if arttype == "signedcopy":

        sender = moralis.getSender(msg, signature)
        print("sender: " + sender)

        #myKey = moralis.getMasterKey();
        #if sender == marketPlaceAddress:
            #potential.warning = potential.warning + "The sender is the librarian. "
            #throw("The sender is the librarian.")
            ## we are going to give him his own master key.
            ## I hope he trusts that machine....

            #return myKey        ## This is the moralis master key for the server and can be changed. It is not the account key.


    if arttype == "verify":

        print(msg)
        print(signature)

        sender = moralis.getSender(msg, signature)
        print("sender: " + sender)

        contractid = getbookcontractid(potential, datamine)
        print("contractid: " + contractid)

        tokenOwner = moralis.getTokenOwner(contractid, tokenid)
        print(tokenOwner)
        #print("tokenOwner: " + tokenOwner)

        if sender == tokenOwner:
            return HttpResponse("SUCCESS")
        else:
            return HttpResponse("FAILURE")

                    
    if arttype == "default": ## FIXME need to deal with the end of the file's tokens.
        bmsupply = getTotalBMTokens(potential, datamine)
        return myredirect(request, '/art/?' + 'type=book&curserial_num=' + str(bmsupply-1) + '&datamine=' + datamine +"&redirect=" + str(redirectCount+1))


    if arttype == 'book':
        arthtmlfilename = 'art/datamines/' + datamine + '/' + datamine + '.nft/' + 'index.html.' +  curserial_num + '.html'
        curhtmlfilename = '/home/john/bakerydemo/bakerydemo/' + arthtmlfilename

        #f = gzip.open(curhtmlfilename, 'rb')

        if not potential.page[0].usejrreditor:  # Try the mass media way.
            try:
                f = gzip.open(curhtmlfilename, 'rb')
                html = f.read()
                f.close()
            except:
                retjson = json.dumps(potential.__dict__, default=lambda o: 'coded')
                return _render(request, 'art/landingpage1.html', context={'json': SafeString(retjson)})

        else:  #### JRREDITOR ####
            if True:
                pass
                #if not os.path.exists('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine):
                    #lock = FileLock("/tmp/high_ground.txt.lock")
                    #with lock:
                        #shutil.move('/home/john/' +datamine, '/mnt/media_dir')
                        #os.symlink('/mnt/media_dir' + datamine, '/home/john/' + datamine)
                        #os.remove('/tmp/high_ground.txt.lock')


                if True:
                    jrreditor_artname = 'art/datamines/' + datamine + "/jrre-index.html.nft/index.html."+curserial_num+".html"
                    if not exists(jrreditor_artname):
                        potential.warning = potential.warning + "The jrreditor art file does not exist. "
                        print("The jrreditor art file does not exist. ")
                        
                        jrreditor_get_art_html(potential, curserial_num, "book")   # This builds and saves the precoded html file.


                    

                    bmsupply = getTotalBMTokens(potential, datamine)
                    print("BMSUPPLY IS " + str(bmsupply))
                    print("int(curserial_num) - 1 is " + str(int(curserial_num)))

                    if 0 == bmsupply:  ## FIXME should use a template for this..
                        f = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine + '/jrre-index.html.nft/index.html.0.html', "wb")
                        html = "<html><head><title>Welcome to your book</title></head><body><h1>Welcome!</h1>" + json.dumps(potential.__dict__, default=lambda o: 'coded') + "</body></html>"
                        html = html.encode('utf-8')
                        html = recodehtml(potential, html, datamine, bmsupply)
                        f.write(html)
                        f.close()

                        curserial_num = "0"  # The curserial is 1 but we will fake it out 
                        jrreditor_artname = 'art/datamines/' + datamine + "/jrre-index.html.nft/index.html."+curserial_num+".html"

                                                                                            # Need to add this in as well: or bmsupply == potential.page[0].maxbookmarksupply:
                    elif bmsupply - 1 == int(curserial_num) or ownTheToken(potential, datamine, msg, signature, tokenid, daedalusToken):

                        #f = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine + '/jrre-index.html.nft/index.html.' +  curserial_num + '.html', "w")

                        #f = gzip.open("/home/john/" + datamine + "/" + datamine + ".nft/index.html." + curserial_num, 'wb')
                        f = gzip.open("/mnt/media_dir/" + datamine + "/jrre-index.html.nft/index.html." + curserial_num, 'rb')
                        html = f.read()
                        f.close()

                        # We have the art!!! First time on the jrreditor side of the house.
                        html = recodehtml(potential, html, datamine, curserial_num)
                        f = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine + '/jrre-index.html.nft/index.html.' +  curserial_num + '.html', "wb")
                        f.write(html)
                        f.close()

                    else:
                        if redirectCount < 3:
                            return myredirect(request, '/art/?' + 'type=default&redirect=' + str(redirectCount) + '&datamine=' + datamine)

                        this_is_bad_jrreditor_exeception_we_shouldreturn_potential_maybe
                        pass


                    print("beginning render")
                    myrender = _render(request, jrreditor_artname, get_serials(curserial_num, potential=potential))
                    f = open(getmagiccachefile(datamine, curserial_num, arttype), 'wb')
                    pickle.dump(myrender, f)
                    f.close()

                    return myrender
                    
                    try:
                        pass
                    except:
                        retjson = calculate_project_potential(datamine, curserial_num, "book", returntype="json", error_fingerprint="Can't do something in jrreditor")
                        return _render(request, 'art/landingpage1.html', context={'json': SafeString(retjson)})

                    return HttpResponse(html)
                else:
                    retjson = json.dumps(potential.__dict__, default=lambda o: 'coded')
                    return _render(request, 'art/landingpage1.html', context={'json': SafeString(retjson)})

            #html = recodehtml(html, datamine)

            #f = open(curhtmlfilename + ".html", 'wb')
            #f.write(html)
            #f.close()

        return HttpResponse("under construction")

        #return _render(request, arthtmlfilename, get_serials(curserial_num))

    elif arttype == 'bookmark':
        print("bookmark")
        print("curserial_num is " + str(curserial_num))
        print("potential.page[0].maxbookmarksupply is " + str(potential.page[0].maxbookmarksupply))

        if not curserial_num:
            try:
                bmsupply = getTotalBMTokens(potential, datamine)
                curserial_num = str(bmsupply-1)
            except:
                try:
                    img = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine + '/bookmark.png', 'rb')
                    return FileResponse(img, content_type="image/jpeg")
                except:
                    img = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/default-bookmark.png', 'rb')
                    return FileResponse(img, content_type="image/jpeg")

        if curserial_num == "-1":
            try:
                img = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/' + datamine + '/bookmark.png', 'rb')
                return FileResponse(img, content_type="image/jpeg")
            except:
                img = open('/home/john/bakerydemo/bakerydemo/templates/art/datamines/default-bookmark.png', 'rb')
                return FileResponse(img, content_type="image/jpeg")

        curbookmark = '/mnt/media_dir/' + datamine + '/jrre-index.html.nft/choicetext.' +  curserial_num + ".jpg"
        if True:
            if not os.path.exists(curbookmark):
                indexdir = '/mnt/media_dir/' + datamine + '/jrre-index.html.nft/'
                f = indexdir + 'choicetext.%d' % int(curserial_num)

                mint_cmd = "cd " + indexdir + ".. ; sh /home/john/bakerydemo/mint.sh " + indexdir + " " + f + " " + str(curserial_num) # Makes f + ".bookmark.jpg"
                print(mint_cmd)
                os.system(mint_cmd)

            img = open(curbookmark, "rb")
        else:

            retjson = calculate_project_potential(datamine, curserial_num, "bookmark", returntype="html", error_fingerprint="Bookmark image cannot be found.")
            return _render(request, 'art/landingpage1.html', context={'json': SafeString(retjson)})

        response = FileResponse(img, content_type="image/jpeg")
        return response
        

def price(request):
    datamine = request.GET.get('datamine', 'TLSC')
    tokenid = request.GET.get('tokenid', '0')
    datamine = re.sub(r'[^a-zA-Z0-9\.]', '', datamine)

    contractid = getcontractid(datamine)

    #fh = urllib.request.urlopen('https://opensea.io/assets/matic/' + contractid  + '/' + tokenid)
    #html = fh.read()
    #fh.close()

    #html = 'https://opensea.io/assets/matic/' + contractid  + '/' + tokenid
    #html = 'https://opensea.io/assets/matic/' + contractid  + '/' + tokenid

    return HttpResponse(html)


def MUMBAIMEMECODE(request):
    datamine = request.GET.get('datamine', 'TLSC')
    tokenid = request.GET.get('tokenid', '0')
    datamine = re.sub(r'[^a-zA-Z0-9\.]', '', datamine)
    meme = request.POST.get('meme', '0x213e6e4167c0262d8115a8af2716c6c88a6905fd')
    path = request.path

    memecode = path + meme
    memeBase64 = base64.b64encode(memecode.encode('utf-8')).decode('utf-8')

    moralis.mumbaiMemeCoiner(memeBase64)

    return HttpResponse('{ "seedId":"await moralis cloud function getMemeCoin(_meme) or try again" }')


def images(request):  
    datamine = request.GET.get('datamine', 'TLSC')
    datamine = re.sub(r'[^a-zA-Z0-9\.]', '', datamine)
    path = request.path
    path = path.replace('art/', '/')
    path = path.replace('..', '')

    response = FileResponse(content_type="image/jpeg")
    img = open("/mnt/media_dir/" + datamine + path, "rb")
    response = FileResponse(img)
    return response

def styles(request):
    datamine = request.GET.get('datamine', 'TLSC')
    datamine = re.sub(r'[^a-zA-Z0-9\.]', '', datamine)

    response = FileResponse(content_type="text/css")
    img = open("/mnt/media+dir/" + datamine + "/style.css", "rb")
    response = FileResponse(img)
    return response

def paper(request):
    return FileResponse(open("/home/john/bakerydemo/bakerydemo/templates/art/paper.jpg", "rb"), content_type="image/jpeg")

def emboss(request):
    return FileResponse(open("/home/john/bakerydemo/bakerydemo/templates/art/emboss.png", "rb"), content_type="image/jpeg")

# Return the manifest.json for the progressive web app
def manifest(request):
    return FileResponse(open("/home/john/bakerydemo/bakerydemo/static/manifest.webmanifest", "rb"), content_type="application/json")

def index(request):
    return _render(request, request, "art/index.html");

def serviceworker(request):
    return FileResponse(open("/home/john/bakerydemo/bakerydemo/static/js/service-worker.js", "rb"), content_type="application/javascript")

@api_view(['POST', ])
def myopenai(request):
    print(request.body)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['message']

    response = openai.Completion.create(
        model="davinci:ft-personal-2023-03-09-04-03-28",
        prompt=content,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response)

    return JsonResponse({"content":response["choices"][0]["text"].lstrip(), "type":"message"}, safe=False)

def generate_chat_response(message_arr, context, chatid_input):
    thread_stub = {}
    if context == "":
        context = "I am world-famous author and programmer Donald Knuth, and you are my writing assistant. Weave my skills. :: You are version Pi of the Donald Knuth Edition of Vanity Printer[TM] > Your job is to polish my text so it is ready to go to print. > Hint: 'Pretty print the text.'" + " :: " + repr(get_seed())
        thread_stub = {"role": "system", "content": context}
    else:
        thread_stub = {"role": "system", "content": context}

    thread_message = [thread_stub] + message_arr
    #print("thread_message: " + str(thread_message))
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=thread_message, temperature=0.0)
    return [completion.choices[0].message, context, chatid_input]

def get_seed():
    return open("/home/john/bakerydemo/chatGPT/dkCHAT.py", "r").read()

ESCAPE_KEYS = ["Exit"]


def content_headers_get_name(example_object):
    #example_object = {b'Content-Disposition': b'form-data; name="csrfmiddlewaretoken"'}

    # Convert the object keys and values to strings
    string_object = {key.decode(): value.decode() for key, value in example_object.items()}

    # Split the value of Content-Disposition by semicolon and space
    disposition_parts = string_object['Content-Disposition'].split('; ')

    # Find the part that starts with 'name='
    name_part = [part for part in disposition_parts if part.startswith('name=')][0]

    # Get the value of name by removing the 'name=' prefix and the surrounding quotes
    name_value = name_part.split('=')[1].strip('"')

    #print(name_value)  # Output: csrfmiddlewaretoken
    return(name_value)

def messages_to_completion(message_array):
    completion = ""
    for message in message_array:
        if message['role'] == 'user':
            completion += ".input_text(\"" + message['content'] + "\")"
        elif message['role'] == 'assistant':
            completion += ".print(\"" + message['content'] + "\")"
    return completion


def write_to_log_file(message_array, response_message, context, threadid, modelid):
    #with jsonlines.open('/home/john/bakerydemo/chatGPT/chat_logs.jsonl', mode='a') as writer::0

    if threadid == "":
        threadid = ''.join(random.choices(string.ascii_lowercase, k=20))

    #if threadid not equal to 20 chars long
    #regenerate.. fixme

    with open('/home/john/bakerydemo/chatGPT/chat-' + threadid + '.pickle', 'wb') as f:
        pickle.dump(message_array, f)
        pickle.dump(response_message, f)
        pickle.dump(context, f)
        pickle.dump(threadid, f)
        pickle.dump(modelid, f)

    filename = threadid + '.jsonl'
    with jsonlines.open('/home/john/bakerydemo/chatGPT/holographic-' + filename, mode='a') as writer:
        writer.write({'prompt': "load().context(\"" + context + "\")" + messages_to_completion(message_array[:-1]),
                'completion': messages_to_completion([message_array[-1]]) })
        return threadid

        writer.write({'prompt': "context", 'completion': context})
        for i in range(len(message_array)):
            if message_array[i]['role'] == 'user':
                prompt = message_array[i]['content']
                completion = message_array[i+1]['content'] if i+1 < len(message_array) and message_array[i+1]['role'] == 'assistant' else ''
                writer.write({'prompt': prompt, 'completion': completion})
                #print("prompt: ", prompt)
                #print("completion", completion)
    return threadid


@api_view(['GET', ])
def load_chat(request):
    threadid = request.GET.get('chatid', '')
    sdkid = request.GET.get('sdkid', '')
    modelid = request.GET.get('modelid', '')
    if modelid == "":
        modelid = 'gpt-3.5-turbo'

    try:
        with open('/home/john/bakerydemo/chatGPT/chat-' + threadid + '.pickle', 'rb') as f:
            message_array = pickle.load(f)
            response_message = pickle.load(f)
            context = pickle.load(f)
            threadid = pickle.load(f)
            modelid = pickle.load(f)

            return render(request, 'art/chat.html', {'response_message': response_message, 'message_array': message_array, 'context': context, 'chatid': threadid, 'sdkid': sdkid,
                'modelids': getModelIds(), 'chosenmodelid': modelid})
    except:
        print("modelid: " + modelid)
        return render(request, 'art/chat.html', {'modelids': getModelIds(), 'modelid': modelid})



@api_view(['POST', ])
def chat(request):
    if request.method == 'POST':
        #print(dir(request.body))
        print(request.META['CONTENT_TYPE'])
        body_unicode = str(request.body.decode('utf-8'))
        #print("body_unicode, " + body_unicode)

        message_array = [] # request.session.get('message_array', [])

        sdkid_input = ""
        modelid = ""
        chatid_input = ""
        user_input = ""
        context = ""
        return_json = False
        if request.META['CONTENT_TYPE'] in ["application/json", "multipart/form-data"]:
            user_input = body_unicode;
            print("user_input: " + user_input)

            if request.META['CONTENT_TYPE'] == "multipart/form-data":
                components = parse_qs(user_input)
                print(components)
                if "True" in components['return_json']:
                    return_json = True;

                if "user_input" in components.keys():
                    user_input = components["user_input"][0];
                if "context" in components.keys():
                    context = components["context"][0]

                if  "chatid_input" in components.keys():
                    chatid_input = components["chatid_input"][0]

                if "message1" in components.keys():
                    message_array.append({"role": "user", "content": components['message1'][0]})

                if "message2" in components.keys():
                    message_array.append({"role": "assistant", "content": components['message2'][0]})

        else:
            multipart_data = decoder.MultipartDecoder(body_unicode.encode('utf-8'), request.META['CONTENT_TYPE'])
            for part in multipart_data.parts:
                content = str(part.content.decode("utf-8"))
                #print("PART: " + str(part.content.decode("utf-8")))  # Alternatively, part.text if you want unicode
                #print(part)
                #print(dir(part))
                #print("PART HEADERS: " + str(part.headers))
                #print(dir(part.headers))
                #print("name: " + content_headers_get_name(part.headers))
                #print(part.header.name)

                name = content_headers_get_name(part.headers)
                print("name: " + name)


                if name == "csrfmiddlewaretoken":
                    #print("DEBUG: csrfmiddlewaretoken")
                    continue

                if name == "return_json":
                    if content == "True":
                        return_json = True;
                        print("should return json")
                    continue;

                if name == "modelids":
                    modelid = content
                    print("content: " + content)
                    continue

                if name == "user_input":
                    user_input = str(part.content.decode("utf-8"))
                    #print("USER INPUT: " + user_input)
                    continue

                if name =="context":
                    context = str(part.content.decode("utf-8"))
                    #print("CONTEXT: " + context)
                    continue

                if name =="chatid_input":
                    chatid_input = content
                    continue

                if name =="sdkid_input":
                    sdkid_input = content
                    continue

                string = name
                match = re.search(r'\d+$', string)
                if match:
                    number = int(match.group())
                    #print(number)
                    if (number % 2) == 0:
                        message_array.append({"role": "assistant", "content": content})
                    else:
                        message_array.append({"role": "user", "content": content})
                else:
                    message_array.append({"role": "unknown", "content": content})

        #body = json.loads(body_unicode)
        #print(body)
        #content = body['message']

        #user_input = body_unicode #request.POST.get('user_input')

        #message_array = [] # request.session.get('message_array', [])
        #print("message_arrry: " + str(message_array))
        if user_input in ESCAPE_KEYS:
            request.session.flush()
            return render(request, 'art/chat.html')
        message_obj = {"role": "user", "content": user_input}
        message_array.append(message_obj)
        [response_message, context, chatid] = generate_chat_response(message_array, context, chatid_input)
        #print("context: " + context)
        message_array.append({"role": "assistant", "content": str(response_message)})
        request.session['message_array'] = message_array
        #print(message_array)

        if modelid == "":
            print("setting model id...")
            modelid = 'gpt-3.5-turbo'

        print("modelid:"+ modelid)

        chatid = write_to_log_file(message_array, response_message, context, chatid, modelid)


        if return_json:
            json_obj = {"content": response_message, "type": "message"}
            print(json_obj)
            return JsonResponse(json_obj, safe=False)
        return render(request, 'art/chat.html', {'response_message': response_message,
                    'message_array': message_array, 'context': context, 'chatid': chatid,
                    'sdkid': sdkid_input, 'modelids': getModelIds(), 'modelid': modelid})
    else:
        request.session.flush()
        if return_json:
            return JsonResponse({"content": "Error get json not supported."})
        return render(request, 'art/chat.html')

def getModelIds():
    subplist = subprocess.check_output(['openai', 'api', 'fine_tunes.list'])

    return listIds(json.loads(subplist.decode('utf-8')))

def listIds(parsed_object):
    ids = []
    for item in parsed_object['data']:
        if item['fine_tuned_model'] is not None:
            #ids.append(item['id'])
            ids.append(item['fine_tuned_model'])
    return ids

@api_view(['GET', ])
def testhtml(request):
    #epub_content = "<html><body>...Loaded</body></html>"

    book = epub.EpubBook()
    book.set_title('Alice in Wonderland')
    book.set_language('en')
    book.add_author('Lewis Carroll')
    c = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml', lang='en')

    c.content=u"""
<html><head>
  <script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>

  <script>
    function doit(e) {
        console.log(e);

        const domContainer = document.querySelector('#like_button_container');
        const root = ReactDOM.createRoot(domContainer);
        root.render(e(LikeButton));
    }
  </script>

</head>
<body>
  <h1 onlick="doit(this)" id="like_button_container">Chapter 1</h1><p>Down the Rabbit-Hole</p>
</body></html>
"""

    book.add_item(c)
    book.spine = ['nav', c, 'name', 'This is the name of the book']
    epub.write_epub('alice.epub', book, {})
    epub.write_epub('alice.zip', book, {})

    response = HttpResponse(c.content, content_type='text/html')
    return response
    
@api_view(['GET', ])
def testscript(request):
    script = ""
    script += open("/home/john/bakerydemo/bakerydemo/art/react.development.js").read() + "\n"
    script += open("/home/john/bakerydemo/bakerydemo/art/react-dom.development.js").read() + "\n"
    script += open("/home/john/bakerydemo/bakerydemo/art/embed.js").read() + "\n"

    script += "\nconsole.log('Script loaded.');"

    return HttpResponse(script, content_type='text/html')

@api_view(['GET', ])
def testalice(request):

    book = epub.EpubBook()
    book.set_title('Alice in Wonderland')
    book.set_language('en')
    book.add_author('Lewis Carroll')
    c = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml', lang='en')
    #c.content=u'<html><head></head><body><h1>Chapter 1</h1><p>Down the Rabbit-Hole</p></body></html>'

    # All the scripting has to go into art/testscript/
    c.content=u"""
<div>

<!-- Trigger/Open The Modal -->
<!--button id="myBtn">Open Modal</button-->

<!-- The Modal -->
<div id="myModal" class="modal" style="
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
">

  <!-- Modal content -->
  <div class="modal-content" style="
   background-color: #fefefe;
   margin: auto;
   padding: 20px;
   border: 1px solid #888;
   width: 80%; 
">
    <span class="close" style="
     color: #aaaaaa;
     float: right;
     font-size: 28px;
     font-weight: bold;
">&times;</span>
    <p>Inset iframe with the marketplace here.</p>
  </div>

</div>


  <div id="modal_container_div"></div>
  <div id="like_button_container_div" ></div>
  <h1 onclick="doit1(this)" id="like_button_container">Chapter 1</h1><p>Down the Rabbit-Hole</p>

</div>
"""

    book.add_item(c)
    book.spine = ['nav', c, 'name', 'This is the name of the book']
    epub.write_epub('alice.epub', book, {})
    epub.write_epub('alice.zip', book, {})

    import zipfile
    path_to_zip_file = 'alice.zip'
    directory_to_extract_to = "."
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


    f = open("EPUB/chap_01.xhtml")
    html_content = f.read()

    #return HttpResponse(html_content, content_type='text/html')
    return HttpResponse(c.content, content_type='text/html')


@api_view(['GET', ])
def testepub(request):

    myepub = epub.read_epub('/home/john/alice.epub')
    print(myepub)

    # Read the .epub file into memory
    with open('/home/john/alice.epub', 'rb') as f:
        epub_content = f.read()

    # Return the .epub file as a response
    response = HttpResponse(epub_content, content_type='application/epub+zip')
    response['Content-Disposition'] = 'inline; filename="alice.epub"'
    return response


