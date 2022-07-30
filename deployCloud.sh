#Deploy the cloud code with the evergrowing BookTradable abi
source .env

source /home/john/wagtailbakerydemo/bin/activate


echo const chainID = \"$chainID\"\; > index.js
cat cloud.js >> index.js
echo const NBT_abi = >> index.js
cat brownie/BookTradable.json >> index.js
echo ";" >> index.js

echo const CC_abi = >> index.js
cat brownie/CultureCoin.json >> index.js
echo ";" >> index.js

echo const nft_market_place_abi = >> index.js
cat brownie/MarketPlace.json >> index.js
echo ";" >> index.js

echo const TGK_abi = >> index.js
cat brownie/TheGoldenKeys.json >> index.js
echo ";" >> index.js


echo const marketPlaceAddress = \"$marketPlaceAddress\"\; >> index.js
echo const cultureCoinAddress = \"$cultureCoinAddress\"\; >> index.js
echo const printingPressAddress = \"$printingPressAddress\"\; >> index.js
echo const daedalusClassBoosterAddress = \"$daedalusClassBoosterAddress\"\; >> index.js
echo const theGoldenKeysAddress = \"$theGoldenKeysAddress\"\; >> index.js
echo const bookRegistryAccount = \"$cCA\"\; >> index.js
echo const placedOfferingsTable = \"$placedOfferings\"\; >> index.js


echo "const marketPlace = new web3.eth.Contract(nft_market_place_abi,marketPlaceAddress);" >> index.js
echo "const cultureCoin = new web3.eth.Contract(CC_abi, cultureCoinAddress);" >> index.js
echo "const theGoldenKey = new web3.eth.Contract(TGK_abi, theGoldenKeysAddress);" >> index.js
echo "const nonceWindow = \"$nonceWindow\";" >> index.js


cp index.js cloudfolder/

### Game CSharp GameEnv.cs
GAMEENV="GameEnv.cs"

echo "namespace MoralisWeb3ApiSdk { public class GameEnv {" > $GAMEENV
echo "public static string timeCubeAddress = \""$timeCubeAddress\"';' >> $GAMEENV
echo "public static string cultureCoinAddress = \""$cultureCoinAddress\"';' >> $GAMEENV
echo "public static string baseSpellsAddress = \""$baseSpellsAddress\"';' >> $GAMEENV
echo "public static string baseLootAddress = \""$baseLootAddress\"';' >> $GAMEENV
echo "public static string bookmarkAddress = \""$bookmarkAddress\"';' >> $GAMEENV
echo "public static string myItemsAddress = \""$myItemsAddress\"';' >> $GAMEENV
echo "public static string heroAddress = \""$heroAddress\"';' >> $GAMEENV
echo "public static string marketPlaceAddress = \""$marketPlaceAddress\"';' >> $GAMEENV
echo "}}" >> $GAMEENV

# deploy the code to the web as well
WEBD="bakerydemo/static/js/defaults.js"
echo Replacing defaults: $WEBD

echo const bookRegistryAddress = \"$marketPlaceAddress\"\; > $WEBD
echo const cultureCoinAddress = \"$cultureCoinAddress\"\; >> $WEBD
echo const printingPressAddress = \"$printingPressAddress\"\; >> $WEBD
echo const daedalusClassBoosterAddress = \"$daedalusClassBoosterAddress\"\; >> $WEBD
echo const theGoldenKeysAddress = \"$theGoldenKeysAddress\"\; >> $WEBD
echo "const nonceWindow = \"$nonceWindow\";" >> $WEBD

echo const serverUrl = \"$serverUrl\"\; >> $WEBD
echo const appId = \"$appId\"\; >> $WEBD
echo const baseNetwork = \"$baseNetwork\"\; >> $WEBD

echo const chainID = \"$chainID\"\; >> $WEBD
echo const chainName = \"$chainName\"\; >> $WEBD
echo const nativeCurrencyName = \"$nativeCurrencyName\"\; >> $WEBD
echo const nativeCurrencySymbol = \"$nativeCurrencySymbol\"\; >> $WEBD
echo const rpcUrls = \"$rpcUrls\"\; >> $WEBD
echo const blockExplorerUrls =  \"$blockExplorerUrls\"\; >> $WEBD
echo const placedOfferingsTable = \"$placedOfferings\"\; >> $WEBD
echo const iRegisterTable = \"$iRegister\"\; >> $WEBD

echo const benDeployAddress = \"$benDeployAddress\"\; >> $WEBD
echo const benScratchesAddress = \"$benScratchesAddress\"\; >> $WEBD
echo const benPettingsTable = \"$benPettings\"\; >> $WEBD

echo const gamblersUnionAddress = \"$gamblersUnionAddress\"\; >> $WEBD
echo const guContestsTable = \"$guContests\"\; >> $WEBD

echo const cc_initial_balance = \"$cc_initial_balance\"\; >> $WEBD
echo const ccTotalSupplyStart = \"$ccTotalSupplyStart\"\; >> $WEBD

# This is for the game...
echo const baseSpellsAddress = \"$baseSpellsAddress\"\; >> $WEBD
echo const baseLootAddress = \"$baseLootAddress\"\; >> $WEBD
echo const myItemsAddress = \"$myItemsAddress\"\; >> $WEBD
echo const heroAddress = \"$heroAddress\"\; >> $WEBD
echo const bookmarkAddress = \"$bookmarkAddress\"\; >> $WEBD
echo const timeCubeAddress = \"$timeCubeAddress\"\; >> $WEBD

echo const BS_abi = >> $WEBD
cat brownie/BaseSpells.json >> $WEBD
echo ";" >> $WEBD

echo const BL_abi = >> $WEBD
cat brownie/BaseLoot.json >> $WEBD
echo ";" >> $WEBD

echo const items_abi = >> $WEBD
cat brownie/MyItems.json >> $WEBD
echo ";" >> $WEBD

echo const hero_abi = >> $WEBD
cat brownie/Hero.json >> $WEBD
echo ";" >> $WEBD

echo const TC_abi = >> $WEBD
cat brownie/TimeCube.json >> $WEBD
echo ";" >> $WEBD


echo const NBT_abi = >> $WEBD
cat brownie/BookTradable.json >> $WEBD
echo ";" >> $WEBD

echo const CC_abi = >> $WEBD
cat brownie/CultureCoin.json >> $WEBD
echo ";" >> $WEBD

echo const nft_market_place_abi = >> $WEBD
cat brownie/MarketPlace.json >> $WEBD
echo ";" >> $WEBD

echo const TGK_abi = >> $WEBD
cat brownie/TheGoldenKeys.json >> $WEBD
echo ";" >> $WEBD

echo const press_abi = >> $WEBD
cat brownie/PrintingPress.json >> $WEBD
echo ";" >> $WEBD

echo const BEN_abi = >> $WEBD
cat brownie/BEN.json >> $WEBD
echo ";" >> $WEBD

echo const GU_abi = >> $WEBD
cat brownie/GamblersUnionBEN.json >> $WEBD
echo ";" >> $WEBD


echo running static collect phase
python3 manage.py collectstatic --noinput

echo make sure to verify the autosavecloud.sh is running...

echo "MEOW! DEPLOYING BEN!"
echo "(cd moralis; . ../.env && node verifyAddon.js $benScratchesAddress $benDeployAddress true)"
(cd moralis; . ../.env && node verifyAddon.js $benScratchesAddress $benDeployAddress true)


