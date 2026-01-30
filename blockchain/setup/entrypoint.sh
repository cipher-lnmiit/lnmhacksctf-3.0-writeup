#!/bin/sh

# Start Hardhat node in the background
npx hardhat node &

# Wait for node to be ready
sleep 5

# Start faucet in the background
node faucet/faucet.js &

# Keep container running
wait
