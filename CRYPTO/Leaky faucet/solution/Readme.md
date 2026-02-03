# Solution to `Leaky Faucet`

The challenge file `challenge.json` needs to be analysed. It contains an LWE (Learning With Errors) cryptosystem with a weak implementation.

The attack exploits three key weaknesses:
1. **Predictable Noise**: The error vector is generated using a Linear Congruential Generator (LCG) with only 13 possible initial states
2. **Known Plaintext**: The flag format `LNMHACKS{` provides 72 bits of known data
3. **Small Parameters**: The modulus q=257 and secret range [-3,4] make the system solvable

Look at the error generation pattern and brute-force all possible LCG states. For each state:
- Regenerate the complete error sequence
- Use the known prefix to remove both error and message from the first 64 equations
- Solve the resulting linear system (A·s = target) over Z₂₅₇ using Gaussian elimination
- Decrypt the full message using the recovered secret key

A python script `solve.py` is provided to show how the extraction can be done.

**Flag:** `LNMHACKS{L0G1C_BE4TS_L4TT1C3S}`