# Connect to the chain, 100 Points

## Author: [bismuth01](https://www.github.com/bismuth01)

## Problem

Chain RPC is given.
Chain ID is given.

Flag format: LNMHACKS{genesis_block_hash}

## Solution

Using either (ethers.js)[https://docs.ethers.org/v5/] or (web3.js)[https://web3js.readthedocs.io/en/v1.10.0/] and get the information for block number 0 to get the genesis hash.

An example script is given using `ethers.js` below.
```js
const ethers = require('ethers');

async function getGenesisBlockHash() {
    try {
        // Connect to the local RPC
        const provider = new ethers.JsonRpcProvider('http://challenges.lnmhacks8.tech/rpc');
        
        // Get the genesis block (block number 0)
        const genesisBlock = await provider.getBlock(0);
        
        if (genesisBlock) {
            console.log('Genesis Block Hash:', genesisBlock.hash);
            console.log('\nFull Genesis Block Info:');
            console.log('Number:', genesisBlock.number);
            console.log('Timestamp:', genesisBlock.timestamp);
            console.log('Parent Hash:', genesisBlock.parentHash);
            console.log('Nonce:', genesisBlock.nonce);
            console.log('Difficulty:', genesisBlock.difficulty);
        } else {
            console.log('Genesis block not found');
        }
    } catch (error) {
        console.error('Error fetching genesis block:', error.message);
    }
}

getGenesisBlockHash();
```

Flag: LNMHACKS{0xe16b03660323b44aad5f3902c4a2d569c38e361d444c62e3e2399d7af470b0aa}