import time
import pytest
import logging
from brownie import accounts
from scripts.helpful_scripts import encode_function_data
LOG = logging.getLogger(__name__)

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

    ##CC.setAddon(bsProxy.address, True, {'from': accounts[0].address})

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

