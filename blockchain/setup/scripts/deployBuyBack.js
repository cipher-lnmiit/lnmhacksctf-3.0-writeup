const { ethers } = require("hardhat");

async function main() {
    const BuyBack = await ethers.getContractFactory("BuyBack");
    const buyBack = await BuyBack.deploy();
    await buyBack.waitForDeployment();

    console.log("BuyBack deployed at:", await buyBack.getAddress());
    console.log("Deployment successful!!");
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });