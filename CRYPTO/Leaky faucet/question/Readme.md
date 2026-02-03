# Leaky Faucet, 350 points

## Author: [KavyaTejpal](__https://github.com/KavyaTejpal__)

## Problem

We intercepted a transmission using LWE (Learning With Errors). The encryption hardware is faulty—the noise generator is "leaking" a repeating pattern.

A challenge file `challenge.json` is given.

## Producing it

Use `leaky_faucet.py` to generate `challenge.json` which is made such that the error/noise vector is generated using a weak Linear Congruential Generator (LCG) with only 13 possible states, making it trivially brute-forceable. The secret key vector has small elements in the range [-3, 4], and the modulus q=257 is deliberately small to make the linear system solvable.