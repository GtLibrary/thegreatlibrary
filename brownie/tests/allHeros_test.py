import time
import pytest
import logging
from brownie import accounts

from greatLibrary_test import CC, MP, PP, example_bookmark, proxyAdmin
from itemsSpellsLoot import  items, spells, loot

LOG = logging.getLogger(__name__)

OneCC = 1000000000000000000   # This number is equal to 1 Culture Coin
maxint = 115792089237316195423570985008687907853269984665640564039457584007913129639935
deployAmount = 2 * 210100027 * OneCC

from scripts.helpful_scripts import encode_function_data

@pytest.fixture(scope="session")
def HEROS(CC, PP, MP, BookTradable, Hero, spells, loot, items, example_bookmark):
    ##address _cCA, address _cultureCoin, address _nbt, address _registryAddress
    hero = accounts[0].deploy(Hero, accounts[0].address, CC.address, example_bookmark.address, MP.address, spells.address, items.address)
    LOG.info("The heros are here: " + str(hero))

    CC.setAddon(hero.address, True, {'from': accounts[0].address})
    hero.setAddon(spells.address, True, {'from': accounts[0].address})
    hero.setAddon(loot.address, True, {'from': accounts[0].address})
    hero.setAddon(items.address, True, {'from': accounts[0].address})
    items.setAddon(hero.address, True, {'from': accounts[0].address})

    return hero

@pytest.fixture(scope="session")
def heros(CC, PP, HEROS, spells):
    nbt = HEROS.getNBT();

    for i in range(1, 150):
        LOG.info("i: " + str(i))
        HEROS.heroMint(1, accounts[0].address, i, 0, {'from': accounts[0].address})

    return HEROS

def test_heros(heros):

    pass

@pytest.fixture(scope="session")
def items(MyItems, CC, MP, spells, example_bookmark):

    ## address _cCA, address _cultureCoin, address _registryAddress, address _baseSpells, address _nbt
    myItems = accounts[0].deploy(MyItems, accounts[0].address, CC.address, MP.address, spells.address, example_bookmark)
    spells.setAddon(myItems.address, True, {'from': accounts[0].address})
    return myItems

@pytest.fixture(scope="session")
def spells(BaseSpells, proxyAdmin, TransparentUpgradeableProxy, Contract, CC):

    BSImpl = accounts[0].deploy(BaseSpells)

    encoded_initializer_function = encode_function_data(BSImpl.initialize, accounts[0].address, CC.address , "Uri")

    proxy = accounts[0].deploy(TransparentUpgradeableProxy,
        BSImpl.address,
        proxyAdmin,
        encoded_initializer_function
    )

    bsProxy = Contract.from_abi("BaseSpells", proxy.address, BaseSpells.abi)
    LOG.info("baseSpells: " + str(bsProxy.address))

    CC.setAddon(bsProxy.address, True, {'from': accounts[0].address})

    return bsProxy

@pytest.fixture(scope="session")
def loot(CC, BaseLoot, proxyAdmin, TransparentUpgradeableProxy, Contract, spells):   #address _cCA, address _cultureCoin, address _baseSpells
    lootImpl = accounts[0].deploy(BaseLoot)
    ## address _cCA, address _cultureCoin, address _baseSpells, string memory _uri
    encoded_initializer_function = encode_function_data(lootImpl.initialize, accounts[0].address, CC.address, spells.address, "Uri")
    proxy = accounts[0].deploy(TransparentUpgradeableProxy,
        lootImpl.address,
        proxyAdmin,
        encoded_initializer_function
    )
    lootProxy = Contract.from_abi("BaseLoot", proxy.address, BaseLoot.abi)
    spells.setAddon(lootProxy.address, True, {'from': accounts[0].address})

    return lootProxy
