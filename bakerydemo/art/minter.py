import os
import re
import shutil

browniedir = "/home/john/bakerydemo/brownie/"
moralisdir = "/home/john/bakerydemo/moralis/"

##jrraymondAddress = "0x213E6E4167C0262d8115A8AF2716C6C88a6905FD"
#lawrenceStanleyAddress = "" # unknown
##cultureCoinAddress = "0xc3bF7d5949C9Bfe74D0222f9C47d2443F181D50B"

cultureCoinAddress = os.environ['cultureCoinAddress']
if not cultureCoinAddress:
    print("Please set the environment variable 'cultureCoinAddress'")
    exit(1)

from bakerydemo.art.moralis import Moralis
moralis = Moralis()


class Minter:
    def __init__(self, potential, datamine, contractType, who):
        self.potential = potential
        self.datamine = datamine
        self._name = contractType + potential._name
        self._symbol = contractType + potential._symbol
        self._bookRegistryAddress = potential._bookRegistryAddress
        self._baseuri = potential._baseuri
        self._burnable = potential._burnable
        self._maxmint = potential._maxmint
        self._defaultprice = potential._defaultprice
        self._defaultfrom = potential._defaultfrom
        self._mintTo = potential._mintTo

        _name = self._name
        _symbol = self._symbol
        _bookRegistryAddress = self._bookRegistryAddress
        _baseuri = self._baseuri
        _burnable = self._burnable
        _maxmint = self._maxmint
        _defaultprice = self._defaultprice  
        _defaultfrom = self._defaultfrom
        _mintTo = self._mintTo

        print("mintTo: " + _mintTo);

        """if moralis.getMarketplace() != _bookRegisteryAddress:
            print("Minter: BookRegisteryAddress is not the same as the one in the Moralis file.")
            moralis.setMarketplace(_bookRegisteryAddress)"""

        """event BookContract(address who, address what);  // <--author,nbt // see culture coin " +
                           "function newBookContract(string memory _name, string memory _symbol, address _bookRegistryAddress, string memory _baseuri, " +
                           "bool _burnable, uint256 _maxmint, uint256 _defaultprice, uint256 _defaultfrom," +
                           "address _mintTo"""
        return moralis.runNewBookContract(_name, _symbol, _bookRegistryAddress, _baseuri, _burnable, _maxmint, _defaultprice, _defaultfrom, _mintTo, who) ##, unknown // moralis got it.



# Shouldnt have to set the gas_limit: "gas_limit": 5000000
deployBookTradable = """
import os
from brownie import *

def main():
    account = accounts.load("Account1")
    print("Account1:", account.address)

    if os.path.exists("%r.force") or not os.path.exists("%r"):

        bt = BookTradable.deploy( 
                "BT%s", "%s", account.address, "http://www.nftbooks.art:9466/nft/%s/", %burnable%, %mintamount%, %mintprice%, %mintfrom%, """ + '"' + cultureCoinAddress + '"' + """,
                {'from': account, "gas_price": 90000000000})
        print("contract deployed at:", bt.address)
        print("Total supply:", bt.totalSupply())

        f = open("%r", "w")
        f.write(bt.address)
        f.close()

        f = open("%r.totalsupply", "w")
        f.write(str(bt.totalSupply()))
        f.close()

        try:
            os.remove("%r.force")
        except:
            pass

    else:
        pass

"""


# Shouldnt have to set the gas_limit: "gas_limit": 5000000
deployCultureCoin = """
import inspect
from brownie import *

OneCC = 10000000000000000000   # This number is equal to 1 Culture Coin

maxint = 115792089237316195423570985008687907853269984665640564039457584007913129639935


def main():
    account = accounts.load("Account1")
    print("Account1:", account.address)


    # Deploy the contract
    print("Deploying the contract...")

    #deployAmount = 100000000 * OneCC
    deployAmount = maxint
    print("Deploying with amount:", deployAmount)

    CultureCoinWrapper.deploy(deployAmount,"""+ cultureCoinAddress +""" , "%meme%", {'from': account, "gas_price": 90000000000})

"""

class MySecondMinter:
    def __init__(self, meme):
        self.meme = meme

    def deploy(self):
        print("Deploying the contract...")


        fs = open(browniedir + "scripts/deploymeme.py", "w")
        deploy = re.sub('%meme%', self.meme, deployCultureCoin)
        fs.write(deploy)
        fs.close()
        
        os.system("cd " + browniedir + " && expect runtx.expect deploymeme.py")

    def myDecoder(self):
        return self.meme 

    def get_meme_code(self):
        return self.myDecoder()


class MyFirstMinter:
    def __init__(self, potential, datamine):
        self.potential = potential
        self.datamine = datamine

        self.startingpoint = potential.startingpoint
        self.bookmarkprice = potential.bookmarkprice
        self.bookprice = potential.bookprice


        self.hardbound = potential.hardbound
        self.hardboundfrom = potential.hardboundfrom
        self.hardboundprice = potential.hardboundprice

        self.authorwallet = potential.authorwallet

        self.name = "MyFirstMinter"

    def getaddoncode(self):
        return ""

    def deployBookContract(self):
        print("Deploying Book Contract for " + self.datamine)

        return self.deployNamedContract("BT" + self.datamine, mintfrom=0, mintprice=self.bookprice)


    def deployBookmarkContract(self):
        print("Deploying Bookmark Contract for " + self.datamine)

        return self.deployNamedContract("BM" + self.datamine, mintfrom=self.startingpoint, mintprice=self.bookmarkprice)


    def deployHardboundContract(self):
        print("Deploying Hardbound Contract for " + self.datamine)

        return self.deployNamedContract("HB" + self.datamine)


    def deployNamedContract(self, name="BMTLSC", minttotal = 1000000000000000000000000, mintfrom=1, mintprice=1): 

        contractfile = "/home/john/" + self.datamine + "/contract" + name + ".txt"

        try:
            os.remove(contractfile + ".failure")
        except:
            pass


        mintamount = minttotal
        if mintamount == "-1" or mintamount == "":
            mintamount = 1000000000000000000000000
        else:
            mintamount = int(mintamount)

        if mintfrom == "":
            mintfrom = mintamount
        else:
            mintfrom = int(mintfrom)

        if mintprice == "":
            mintprice = 1000000000000000000000000
            mintfrom = mintamount   ## Reseting harboundfrom if price is not set.
        else:
            mintprice = mintprice


        deploy = re.sub('%s', name, deployBookTradable)
        deploy = re.sub('%r', contractfile, deploy)
        deploy = re.sub('%burnable%', "True", deploy)               # Burnable so watch out.
        deploy = re.sub('%mintamount%', str(mintamount), deploy)    # Max mintable.
        deploy = re.sub('%mintfrom%', str(mintfrom), deploy)        # Starting point.
        deploy = re.sub('%mintprice%', str(mintprice), deploy)      # Price after start.
        print(deploy)

        f = open(browniedir + "scripts/deployBT" + name + ".py", "w")
        f.write(deploy)
        f.close()

        os.system("cd " + browniedir + " && expect launch.expect deployBT" + name + ".py")

        transfercmd = "cd " + moralisdir + " && node transferContractOwner.js " + contractfile + " " + self.authorwallet
        print(transfercmd)
        f = open(contractfile + ".transfercmd", "w")
        f.write(transfercmd)
        f.close()

        os.system(transfercmd)

        if os.path.exists(contractfile + ".failure"):
            print("Failed to deploy " + name + " contract.")
            return False
        else:
            print("Successfully deployed " + name + " contract.")
            return True

