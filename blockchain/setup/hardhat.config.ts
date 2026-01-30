import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import * as dotenv from "dotenv";

dotenv.config({quiet: true});

const FAUCET_PRIVATE_KEY = process.env.FAUCET_PRIVATE_KEY || "";

if (FAUCET_PRIVATE_KEY == "") {
  throw new Error('FAUCET_PRIVATE_KEY Not Found');
}

const config: HardhatUserConfig = {
  solidity: "0.8.28",
  networks: {
    hardhat: {
      chainId: 1337,
      mining: {
        auto: true,
        interval: 10000
      },
      accounts: [
        {
          privateKey: FAUCET_PRIVATE_KEY,
          balance: "100000000000000000000000000"
        }
      ],
      initialDate: "2024-01-01T00:00:00Z",
    }
  }
};

export default config;
