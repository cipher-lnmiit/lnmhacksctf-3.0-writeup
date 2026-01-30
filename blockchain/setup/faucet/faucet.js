const express = require("express");
const { ethers } = require("ethers");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const dotenv = require("dotenv");
const path = require("path");

dotenv.config();

const FAUCET_PRIVATE_KEY = process.env.FAUCET_PRIVATE_KEY;
const FAUCET_PORT = Number(process.env.FAUCET_PORT || 3000);

if (!FAUCET_PRIVATE_KEY) throw new Error("FAUCET_PRIVATE_KEY missing");

const app = express();

/* ---------- middleware ---------- */
app.use(express.json());
app.use(express.static(__dirname)); // ✅ SERVE HTML + JS
app.use(helmet());

/* ---------- hardhat ---------- */
const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
const faucet = new ethers.Wallet(FAUCET_PRIVATE_KEY, provider);
const DRIP_AMOUNT = "10";

/* ---------- anti-abuse ---------- */
const claimed = new Set();

const limiter = rateLimit({
  windowMs: 5 * 60 * 1000,
  max: 5
});

/* ---------- routes ---------- */
app.get("/", (_, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/faucet", limiter, async (req, res) => {
  const { address } = req.body;

  if (!ethers.isAddress(address)) {
    return res.status(400).json({ dripStatus: "invalid" });
  }

  if (claimed.has(address)) {
    console.log(`Already claimed by ${address}`);
    return res.status(400).json({ dripStatus: "already claimed" });
  }

  try {
    const tx = await faucet.sendTransaction({
      to: address,
      value: ethers.parseEther(DRIP_AMOUNT)
    });

    await tx.wait();
    claimed.add(address);

    console.log(`Dripped to ${address}`);
    return res.json({
      dripStatus: "success",
      txHash: tx.hash
    });
  } catch (err) {
    console.log(`Failed ${address}`);
    return res.status(500).json({
      dripStatus: "fail",
      error: err.message
    });
  }
});

/* ---------- start ---------- */
app.listen(FAUCET_PORT, () => {
  console.log(`Faucet running on http://localhost:${FAUCET_PORT}`);
});
