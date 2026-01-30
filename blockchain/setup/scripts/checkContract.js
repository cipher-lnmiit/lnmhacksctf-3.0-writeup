const { ethers } = require("ethers");

async function main() {
    // Get RPC and address from command line arguments
    const rpcUrl = "http://challenges.lnmhacks8.tech/rpc";
    const address = "0xa1b77ae1EFF15A165A5D9Ca2e658B52f7E165C7A";

    if (!rpcUrl || !address) {
        console.error("Usage: node scripts/checkContract.js <rpc_url> <address>");
        console.error("Example: node scripts/checkContract.js http://127.0.0.1:8545 0x1234...");
        process.exit(1);
    }

    // Validate address format
    if (!ethers.isAddress(address)) {
        console.error("Error: Invalid Ethereum address");
        process.exit(1);
    }

    console.log(`RPC URL: ${rpcUrl}`);
    console.log(`Checking address: ${address}`);

    // Connect to the provider
    const provider = new ethers.JsonRpcProvider(rpcUrl);

    // Get the bytecode at the address
    const code = await provider.getCode(address);

    // If code is "0x", no contract exists (it's an EOA or empty address)
    if (code === "0x") {
        console.log("❌ No contract exists at this address");
        console.log("This is either an externally owned account (EOA) or an unused address");
    } else {
        console.log("✅ Contract exists at this address");
        console.log(`Bytecode length: ${code.length - 2} bytes`); // -2 for "0x" prefix
        console.log(`Bytecode preview: ${code.substring(0, 66)}...`); // First 32 bytes
    }
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
