const tools = require('./tools');
const fs = require('fs');
const https = require('https');
const lockFile = require('lockfile')
const readline = require('readline');

const myArgs = process.argv.slice(2);
const portNum = myArgs[0];
const bindAddr = myArgs[1];
const remoteAddrs = process.argv.slice(4);
console.log("port: ", portNum);
console.log("addr: ", bindAddr);



process.on('SIGINT', () => {	// FIXME: readline is catching the first control+c for some reason...
	process.exit();
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl._writeToOutput = function _writeToOutput(stringToWrite) {
	rl.output.write("\x1B[2K\x1B[200D"+"["+((rl.line.length%2==1)?"=-":"-=")+"]");
};

rl.question('pass: ', (passPhrase) => {
	console.log();		// Because of ugliness and no time to put makeup on this hog. Dont delete until better password handling in in place.
	runServer(passPhrase);
});

function runServer(passPhrase) {

	const metakeycontent = tools.cCAPrivateKeyEncrypted.split(":");
	const metakeycon = {iv: metakeycontent[0], content: metakeycontent[1]};
	//console.debug("DEBUG:", metakeycon);
	
	const cCAPrivateKey = tools.decrypt(passPhrase, metakeycon);
	//console.debug("DEBUG: cCAPrivateKey: ", cCAPrivateKey);

	tools.cCAPrivateKey = cCAPrivateKey;

	const options = {
  		key: fs.readFileSync('key.pem'),
  		cert: fs.readFileSync('cert.pem'),
  		passphrase: passPhrase
	};

	const server = https.createServer(options, async (req, res) => {
  		res.writeHead(200);

		console.log("remote: ", req.connection.remoteAddress);

		if(remoteAddrs.includes(req.connection.remoteAddress)) {
			console.log("Remote address is good.");
		} else {
			console.log("Remote address is bad.");
		}

		const restfulCmd = req.url.split('/');

        	const address = restfulCmd[1]; // The contract address of interest
        	console.log('address', address);
        	const cmd = restfulCmd[2];
        	console.log('cmd', cmd);        // The command to run on it...

        	if(cmd === 'totalsupply') {
                	try {
                        	ts = await tools.getTotalSupply(address);
                        	//res.send(ts);
                        	res.end(ts);
                	} catch(e) {
                        	console.log('Error', e);
                        	//res.send(e);
                        	res.end(e);
                	}
        	} else if(cmd === 'verifyrewards') {
                	try {
                        	const child = restfulCmd[3];
                        	console.log('child', child);

                        	const verified = await tools.verifyRewardContract(address, child, cCAPrivateKey);
                        	let addonRet = await tools.setupAddonPrintingPress(address, cCAPrivateKey);

                        	console.log("addonRet: ", addonRet);
                        	addonRet = await tools.setupAddonPrintingPress(child, cCAPrivateKey);
                        	console.log("addonRet: ", addonRet);
                        	//res.send("verified");
				res.end("verified");

                	} catch(e) {
                        	console.log('Error', e);
                        	//res.send(e);
				res.end(e);
                	}
		//secureUri = "0x0" + "/newbookcontract/" + _name + "/" + _symbol+ "/" + _bookRegistryAddress + "#" + _baseuri + "#"
    		//secureUri += _burnable + "/" + _maxmint + "/" + _defaultprice + "/" + _defaultfrom + "/" + _mintTo + "#" + whoFile
		// Contract is 0x0 for creation calls.
        	} else if(cmd === 'newbookcontract') {
			console.log(req.url);
			const newBookCmdPart1 = req.url.split('!');
			console.log(newBookCmdPart1);

			const whoFile = newBookCmdPart1[3];
			console.log(whoFile);

			// /0x0/newbookcontract/BMMBMPGBRRR/BMMBMPGBRRR/0x17a3D635284c100ea39f2Eb294AeB40CC87f3c23

			const newBookCmdPart2 = newBookCmdPart1[0].split('/');
			const newBookCmdPart3 = newBookCmdPart1[2].split('/');

			const _name = newBookCmdPart2[3];
			const _symbol = newBookCmdPart2[4];
			const _bookRegistryAddress = newBookCmdPart2[5];

			const _baseuri = newBookCmdPart1[1];
			
			const _burnable = newBookCmdPart3[0];
			const _maxmint = newBookCmdPart3[1];
			const _defaultprice = newBookCmdPart3[2];
			const _defaultfrom = newBookCmdPart3[3];
			const _mintTo = newBookCmdPart3[4];
			//const who = myArgs[9];


        		var contractid;		// This will be the real contract when the tx completes.
			await newBookContractWithLockFile(whoFile, _name, _symbol, _bookRegistryAddress, _baseuri, _burnable, _maxmint, _defaultprice, _defaultfrom, _mintTo, cCAPrivateKey);
			res.end();
		} else {
			res.end();
		}

	
  		//res.end();
	});

	server.listen(portNum, bindAddr, () => {
  		console.log(`Server running at http://${bindAddr}:${portNum}/`);
  
	});
}


async function newBookContractWithLockFile(whoFile, _name, _symbol, _bookRegistryAddress, _baseuri, _burnable, _maxmint, _defaultprice, _defaultfrom, _mintTo, cCAPrivateKey) {

	const defaultPrice = tools.web3.utils.toWei(_defaultprice,"ether");

	const txsFile = whoFile + ".txs";

        try {
                // Read the file's string contents directly into the contractid
                const ret = await tools.newBookContract(_name, _symbol, _bookRegistryAddress, _baseuri, _burnable, _maxmint, defaultPrice, _defaultfrom, _mintTo, cCAPrivateKey);
		console.log("ret: ", ret);
		//console.log("who: ", who);
		console.log("whoFile: ", whoFile);


		const typesArray = [
                                {type: 'string', name: '_meme'},
                                {type: 'uint256', name: 'amount'},
                                {type: 'address', name: 'what', indexed: true},
                                //{type: 'string', name: 'crypt'},
                        ];

		const result = ret;
		//console.log("result: ", result);
		//console.log("result.logs: ", result.logs);

		const txs = result.logs[2].transactionHash;
		console.log("txs: ", txs);

		const contractid = await tools.getContractId(txs);
		console.log("contractid: ", contractid);
		if(contractid != "check moralis query string above and the id of the registry in your moralis server.") {
			console.log("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEE");
			console.log(contractid, contractid, contractid, contractid, contractid);
			console.log(whoFile)
			tools.writeFile(whoFile, contractid);
			tools.writeFile(whoFile + ".totalsupply", "0");

			for(i=0; i<10; i++) {
				try {
					const addonRet = await tools.setupAddonPrintingPress(contractid, cCAPrivateKey);
					console.log("addonRet: ", addonRet);
					break;

				} catch(e) {
					console.log("Error adding on addon: ", e);
					tools.sleep(1000);
				}
			}
		}

        } catch (e) {
                console.log('error calling newBookContract: ',  e);
		//tools.writeFile(retTxt, e);
                return;
        }
}

