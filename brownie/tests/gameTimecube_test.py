from brownie import accounts
from greatLibrary_test import LOG, CC, proxyAdmin, PP, MP, HEROS, example_bookmark, heros, spells, loot, items, timecube, FLAG_IS_NPC, DAEDALUSCLASS, DAEDALUS, ARCANE_ORB, HERO_MINT_MAX

GAZ=1       # These are the hero's token id's
RENNLY=15   # They should be sized to the HEROS from the greatlLibrary
def test_scenario(heros, spells, loot, items, timecube):
    ## GAZ cast Arcane Orb on himself twice and Rennly one.

    hpVals = heros.getHP(GAZ)
    LOG.info("hpVals")
    LOG.info(hpVals.return_value)

    while int(hpVals.return_value[0]) > 0:
        spells.castAO(heros.address, GAZ, GAZ, RENNLY, {'from': accounts[0].address})
        LOG.info("Gaz cast Arcane Orb on himself twice and Rennly once.")
        ## Rennly activates the arcane orb attacking gaz with it.
        loot.activateAO(heros.address, RENNLY, GAZ, ARCANE_ORB, 1, {'from': accounts[0].address})
        LOG.info("Rennly activates his arcane orb attacking Gaz with it.")

        hpVals = heros.getHP(GAZ)
        LOG.info("hpVals")
        LOG.info(hpVals.return_value[0])

    ## GAZ is dead, so Rennly loots him.
    loot.loot(heros.address, RENNLY, GAZ, {'from': accounts[0].address})
    LOG.info("Gaz is dead, so Rennly loots him.")

    ## DAEDALUS reesurects GAZ.
    timecube.castRES(DAEDALUS, GAZ, {'from': accounts[0].address})
    LOG.info("Daedalus reesurects Gaz.")

    # transmute(uint256 _hId, int _slot, uint _time, uint _what, uint _amount)
    ## Rennly transmutes the loot off Gaz in the cube
    timecube.transmute(RENNLY, 1, 1, GAZ, 1, {'from': accounts[0].address})
    LOG.info("Rennly transmutes the loot he got off Gaz in the cube.")
