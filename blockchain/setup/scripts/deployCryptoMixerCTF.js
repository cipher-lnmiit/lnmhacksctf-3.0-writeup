const { ethers } = require("hardhat");

async function main() {
    console.log("Deploying CryptoMixer CTF Challenge...\n");

    // Get signers
    const signers = await ethers.getSigners();
    
    // Create additional wallets for the CTF
    const deployer = signers[0];
    const user1 = ethers.Wallet.createRandom().connect(ethers.provider);
    const user2 = ethers.Wallet.createRandom().connect(ethers.provider);
    const user3 = ethers.Wallet.createRandom().connect(ethers.provider);
    const targetUser = ethers.Wallet.createRandom().connect(ethers.provider);
    const recv1 = ethers.Wallet.createRandom().connect(ethers.provider);
    const recv2 = ethers.Wallet.createRandom().connect(ethers.provider);
    const recv3 = ethers.Wallet.createRandom().connect(ethers.provider);
    const recv4 = ethers.Wallet.createRandom().connect(ethers.provider);
    
    console.log("Deployer:", await deployer.getAddress());
    console.log("Target User (vulnerable):", await targetUser.getAddress());
    
    // Fund the test accounts
    console.log("\n💰 Funding test accounts...");
    await deployer.sendTransaction({ to: await user1.getAddress(), value: ethers.parseEther("20") });
    await deployer.sendTransaction({ to: await user2.getAddress(), value: ethers.parseEther("20") });
    await deployer.sendTransaction({ to: await user3.getAddress(), value: ethers.parseEther("20") });
    await deployer.sendTransaction({ to: await targetUser.getAddress(), value: ethers.parseEther("20") });
    console.log("✅ Accounts funded\n");
    
    // Deploy the mixer
    const CryptoMixer = await ethers.getContractFactory("CryptoMixer");
    const mixer = await CryptoMixer.deploy();
    await mixer.waitForDeployment();
    const mixerAddress = await mixer.getAddress();
    
    console.log("\n✅ CryptoMixer deployed at:", mixerAddress);
    
    // Disable auto-mining to batch transactions
    await ethers.provider.send("evm_setAutomine", [false]);
    
    // Simulate normal mixer activity - multiple users deposit in same block
    console.log("\n📦 Preparing Block: Multiple users deposit (normal behavior)");
    await mixer.connect(user1).deposit({ value: ethers.parseEther("5") });
    await mixer.connect(user2).deposit({ value: ethers.parseEther("3") });
    await ethers.provider.send("evm_mine");
    console.log("  ✅ User1 and User2 deposited together");
    
    // Mine some empty blocks
    await ethers.provider.send("evm_mine");
    await ethers.provider.send("evm_mine");
    
    // Another normal block
    console.log("\n📦 Preparing Block: Multiple users deposit again");
    await mixer.connect(user3).deposit({ value: ethers.parseEther("2") });
    await mixer.connect(user1).deposit({ value: ethers.parseEther("1") });
    await ethers.provider.send("evm_mine");
    console.log("  ✅ User3 and User1 deposited together");
    
    // Mine empty blocks
    await ethers.provider.send("evm_mine");
    await ethers.provider.send("evm_mine");
    
    // THE VULNERABLE BLOCK - Only target user deposits
    console.log("\n📦 Preparing Block: ⚠️  ONLY ONE USER DEPOSITS (vulnerable!)");
    const txTarget = await mixer.connect(targetUser).deposit({ value: ethers.parseEther("10") });
    await ethers.provider.send("evm_mine");
    const receipt = await ethers.provider.getTransactionReceipt(txTarget.hash);
    console.log("  ⚠️  Target user deposited 10 ETH ALONE!");
    console.log("  - Block number:", receipt.blockNumber);
    console.log("  - Target address:", await targetUser.getAddress());
    
    // Mine empty blocks
    await ethers.provider.send("evm_mine");
    await ethers.provider.send("evm_mine");
    
    // Normal activity continues
    console.log("\n📦 Preparing Block: More normal deposits");
    await mixer.connect(user2).deposit({ value: ethers.parseEther("4") });
    await ethers.provider.send("evm_mine");
    console.log("  ✅ User2 deposited");
    
    // Mine empty block
    await ethers.provider.send("evm_mine");
    
    // Target user withdraws to multiple addresses with flag parts
    console.log("\n💸 Target user withdraws to multiple addresses (with flag parts hidden)");
    
    const recipients = [
        await recv1.getAddress(),
        await recv2.getAddress(),
        await recv3.getAddress(),
        await recv4.getAddress()
    ];
    
    const amounts = [
        ethers.parseEther("2.5"),
        ethers.parseEther("2.5"),
        ethers.parseEther("2.5"),
        ethers.parseEther("2.5")
    ];
    
    // Flag parts hidden in data field
    const flagParts = [
        ethers.toUtf8Bytes("LNMHACKS{tr4ck"),
        ethers.toUtf8Bytes("3d_thr0ugh"),
        ethers.toUtf8Bytes("_s1ngl3_bl"),
        ethers.toUtf8Bytes("0ck_d3p0s1t}")
    ];
    
    const withdrawTx = await mixer.connect(targetUser).withdraw(recipients, amounts, flagParts);
    await ethers.provider.send("evm_mine");
    const withdrawReceipt = await ethers.provider.getTransactionReceipt(withdrawTx.hash);
    console.log("  - Withdrew to", recipients.length, "addresses");
    console.log("  - Transaction:", withdrawReceipt.hash);
    
    // Re-enable auto-mining
    await ethers.provider.send("evm_setAutomine", [true]);
    
    // Summary
    console.log("\n" + "=".repeat(60));
    console.log("CTF CHALLENGE SETUP COMPLETE");
    console.log("=".repeat(60));
    console.log("\n📝 Challenge Description:");
    console.log("A crypto mixer has been operating on this blockchain.");
    console.log("Due to a privacy leak, one user deposited alone in a block.");
    console.log("Track down their withdrawals and extract the flag!\n");
    console.log("🎯 Mixer Contract:", mixerAddress);
    console.log("🔍 Hint: Look for blocks with only one depositor");
    console.log("🚩 Flag format: FLAG{...}\n");
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
