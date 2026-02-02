# The Chronos Gamble ⏳

## Premise
The Great Clock of Chronos governs all outcomes in this realm. To the uninitiated, the numbers it produces are pure chaos. But to those who understand that time is the only source of truth, the future is written in the seconds. 

Synchronize your heartbeat with the machine, predict 30 steps into the future, and the vault will open.

## Challenge Type
- **Category:** Binary Exploitation (Pwn) / Reverse Engineering
- **Difficulty:** Easy/Medium
- **Tags:** PRNG, Time-sync, Linux-C

## Infrastructure Setup
This challenge is containerized using Docker for easy deployment and isolation.

### Prerequisites
- Docker
- Docker Desktop (if on Windows/macOS)

### Local Deployment
To host the challenge locally for testing or a private CTF:

1. **Build the image:**
   ```bash
   docker build -t chronos-gamble .
