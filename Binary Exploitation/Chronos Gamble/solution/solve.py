from pwn import *
from ctypes import CDLL
import time

# This loads the C library so Python can use the exact same rand() as your C program
libc = CDLL("libc.so.6")

def solve():
    try:
        # 1. Connect to your running Docker container
        io = remote('localhost', 1337)
        
        # 2. Get the current Unix Time (The Seed)
        # We sync our local PRNG with the server's seed
        now = int(time.time())
        libc.srand(now)
        
        print(f"[*] Synchronized with system time: {now}")
        
        # 3. Predict the 30 numbers
        for i in range(30):
            # We use the same 'rand() & 0xf' logic from your challenge.c
            target = libc.rand() & 0xf
            
            # Send the number to the server
            io.sendlineafter(b"Prediction: ", str(target).encode())
            print(f"[+] Round {i+1}: Sent {target}")

        # 4. Catch the flag!
        success_message = io.recvall().decode()
        print("\n" + "="*20)
        print(success_message)
        print("="*20)

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    solve()
