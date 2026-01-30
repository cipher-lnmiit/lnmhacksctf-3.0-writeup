# Hardhat Node & Faucet setup

The Hardhat Node starts with a fixed config that is specified in `hardhat.config.ts`.

The Faucet is at the `faucet` directory which is a protected express server which servers a simple web page.

The whole think can be directly started with docker using `FAUCET_PRIVATE_KEY=<your_faucet_private_key> docker compose up -d`.

All contracts are deployed afterwards after entering the blockchain container using `docker exec -it <docker_container_name> sh` and using `npx hardhat run scripts/<deploy_script> --network localhost`.
This setup let's deploy new contracts and maintain in the live environment.

But the chain setup also has `auto_mine=true` which essentially automatically mines a block instantly to add a transaction which forces the participants to write attacking contracts rather than attack directly through the chain RPC.