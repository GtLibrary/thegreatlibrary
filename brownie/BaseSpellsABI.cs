namespace MoralisWeb3ApiSdk { public class BaseSpellsABI { public static string ABI = "[{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"approved\",\"type\":\"bool\"}],\"name\":\"ApprovalForAll\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256[]\",\"name\":\"ids\",\"type\":\"uint256[]\"},{\"indexed\":false,\"internalType\":\"uint256[]\",\"name\":\"values\",\"type\":\"uint256[]\"}],\"name\":\"TransferBatch\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"TransferSingle\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"string\",\"name\":\"value\",\"type\":\"string\"},{\"indexed\":true,\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"URI\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_yards\",\"type\":\"uint256\"}],\"name\":\"_yards\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"addExperience\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_gM\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_what\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"addonMintTo\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"addonPay\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"name\":\"balanceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address[]\",\"name\":\"accounts\",\"type\":\"address[]\"},{\"internalType\":\"uint256[]\",\"name\":\"ids\",\"type\":\"uint256[]\"}],\"name\":\"balanceOfBatch\",\"outputs\":[{\"internalType\":\"uint256[]\",\"name\":\"\",\"type\":\"uint256[]\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"burn\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"internalType\":\"uint256[]\",\"name\":\"ids\",\"type\":\"uint256[]\"},{\"internalType\":\"uint256[]\",\"name\":\"values\",\"type\":\"uint256[]\"}],\"name\":\"burnBatch\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_to1\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_to2\",\"type\":\"uint256\"}],\"name\":\"castAO\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_beastCount\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"_petType\",\"type\":\"int256\"},{\"internalType\":\"uint256\",\"name\":\"ccAmount\",\"type\":\"uint256\"}],\"name\":\"castSB\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_to\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"_what\",\"type\":\"int256\"},{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"castTo\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"}],\"name\":\"curSummons\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"_resist\",\"type\":\"int256\"}],\"name\":\"damageFloor\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_x\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_ten\",\"type\":\"uint256\"}],\"name\":\"dot\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_addon\",\"type\":\"address\"}],\"name\":\"getAddon\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"getHPBase\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"}],\"name\":\"getLevel\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"getPowBase\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_power\",\"type\":\"uint256\"}],\"name\":\"getPowerMult\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_power\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_powerMax\",\"type\":\"uint256\"}],\"name\":\"getPowerShift\",\"outputs\":[{\"internalType\":\"int256\",\"name\":\"\",\"type\":\"int256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"}],\"name\":\"getSkin\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"getStamMult\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"_which\",\"type\":\"int256\"}],\"name\":\"getState\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"}],\"name\":\"getXYZ\",\"outputs\":[{\"components\":[{\"internalType\":\"int256\",\"name\":\"hX\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hY\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hZ\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hAlpha\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hBeta\",\"type\":\"int256\"}],\"internalType\":\"struct HeroXYZ\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"\",\"type\":\"int256\"}],\"name\":\"hState\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"hasLOS\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_x\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_ten\",\"type\":\"uint256\"}],\"name\":\"hot\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_cCA\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"cultureCoin\",\"type\":\"address\"},{\"internalType\":\"string\",\"name\":\"_uri\",\"type\":\"string\"}],\"name\":\"initialize\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"isAddon\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"}],\"name\":\"isApprovedForAll\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"x\",\"type\":\"uint256\"}],\"name\":\"log2\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"y\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"}],\"name\":\"maxSummon\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_curHp\",\"type\":\"uint256\"},{\"components\":[{\"internalType\":\"bool\",\"name\":\"needsTightening\",\"type\":\"bool\"},{\"internalType\":\"address\",\"name\":\"hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"target\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"heal\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"damage\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"damageType\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"armor\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"fire\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"frost\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"meta\",\"type\":\"int256\"},{\"internalType\":\"uint256\",\"name\":\"effect\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"interval\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"curTicks\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"startTime\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"maxTicks\",\"type\":\"uint256\"}],\"internalType\":\"struct Screwdrivers\",\"name\":\"_nutsNBolts\",\"type\":\"tuple\"}],\"name\":\"resolveHP\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256[]\",\"name\":\"ids\",\"type\":\"uint256[]\"},{\"internalType\":\"uint256[]\",\"name\":\"amounts\",\"type\":\"uint256[]\"},{\"internalType\":\"bytes\",\"name\":\"data\",\"type\":\"bytes\"}],\"name\":\"safeBatchTransferFrom\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"data\",\"type\":\"bytes\"}],\"name\":\"safeTransferFrom\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_addon\",\"type\":\"address\"},{\"internalType\":\"bool\",\"name\":\"_onOff\",\"type\":\"bool\"}],\"name\":\"setAddon\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"operator\",\"type\":\"address\"},{\"internalType\":\"bool\",\"name\":\"approved\",\"type\":\"bool\"}],\"name\":\"setApprovalForAll\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"}],\"name\":\"setSkin\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"_which\",\"type\":\"int256\"},{\"internalType\":\"bool\",\"name\":\"_state\",\"type\":\"bool\"}],\"name\":\"setState\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"int256\",\"name\":\"_x\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"_y\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"_z\",\"type\":\"int256\"}],\"name\":\"setXYZ\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"shadowTag\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"int256\",\"name\":\"x\",\"type\":\"int256\"}],\"name\":\"sqrt\",\"outputs\":[{\"internalType\":\"int256\",\"name\":\"y\",\"type\":\"int256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes4\",\"name\":\"interfaceId\",\"type\":\"bytes4\"}],\"name\":\"supportsInterface\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"tag\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"}],\"name\":\"tagged\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"uri\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"internalType\":\"int256\",\"name\":\"hX\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hY\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hZ\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hAlpha\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hBeta\",\"type\":\"int256\"}],\"internalType\":\"struct HeroXYZ\",\"name\":\"one\",\"type\":\"tuple\"},{\"components\":[{\"internalType\":\"int256\",\"name\":\"hX\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hY\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hZ\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hAlpha\",\"type\":\"int256\"},{\"internalType\":\"int256\",\"name\":\"hBeta\",\"type\":\"int256\"}],\"internalType\":\"struct HeroXYZ\",\"name\":\"two\",\"type\":\"tuple\"}],\"name\":\"xyzDist\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_hero\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_hId\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_target\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_maxRange\",\"type\":\"uint256\"}],\"name\":\"xyzInRange\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]"; } }