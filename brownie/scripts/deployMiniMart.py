import os
import inspect
from brownie import *

from dotenv import load_dotenv
load_dotenv()

cultureCoinAddress = os.environ['cultureCoinAddress']
print("cuturecoin: " + cultureCoinAddress)

def main():
    account = accounts.load("Account1")
    print("Account1:", account.address)
    print("Balance:", account.balance())
    print("Nonce:", account.nonce)

    # Deploy the contract
    print("Deploying the contract...")

    #market = MarketPlace[len(MarketPlace) - 1]

    market = MiniMart.deploy(account.address, account.address, cultureCoinAddress, {'from': account}) # , "gas_price": gasPrice})
    print("MiniMart deployed at:" + market.address)
