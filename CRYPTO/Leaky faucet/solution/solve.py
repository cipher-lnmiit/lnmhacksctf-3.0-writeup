import numpy as np
import json

def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return None

def solve():
    with open("challenge.json", "r") as f:
        data = json.load(f)
    A = np.array(data["A"])
    b = np.array(data["b"])
    q = 257
    n = 64

    # The Known Plaintext: LNMHACKS{
    prefix = "LNMHACKS{"
    prefix_bits = "".join([format(ord(c), '08b') for c in prefix])
    # We use exactly 64 bits to match the length of vector 's'
    prefix_msg = [int(b) * (q // 2) for b in prefix_bits[:n]]

    print("Brute-forcing LCG states and solving linear system...")

    for start_state in range(13):
        state = start_state
        e = []
        for _ in range(len(b)):
            state = (state * 5 + 1) % 13
            e.append(state - 6)
        e = np.array(e)

        # Remove error and prefix bits to isolate 'As' for the first 64 rows
        target = (b - e) % q
        for i in range(len(prefix_msg)):
            target[i] = (target[i] - prefix_msg[i]) % q

        try:
            # Solve As = target using Gaussian Elimination (mod 257)
            M = A[:n].copy().tolist()
            V = target[:n].copy().tolist()
            
            for i in range(n):
                inv = modInverse(M[i][i], q)
                if inv is None: continue
                for j in range(i + 1, n):
                    factor = (M[j][i] * inv) % q
                    V[j] = (V[j] - factor * V[i]) % q
                    for k in range(i, n):
                        M[j][k] = (M[j][k] - factor * M[i][k]) % q

            s_recovered = [0] * n
            for i in range(n - 1, -1, -1):
                summ = sum(M[i][j] * s_recovered[j] for j in range(i + 1, n))
                s_recovered[i] = ((V[i] - summ) * modInverse(M[i][i], q)) % q

            # Now unmask the full flag
            final_scaled = (b - np.dot(A, s_recovered) - e) % q
            bits = "".join(["1" if (q//4 < v < 3*q//4) else "0" for v in final_scaled])
            
            recovered_flag = ""
            for i in range(0, len(bits), 8):
                recovered_flag += chr(int(bits[i:i+8], 2))
            
            if "LNMHACKS{" in recovered_flag:
                print("\n[+] FLAG FOUND!")
                print(f"Seed Index: {start_state}")
                print(f"Result: {recovered_flag}")
                return
        except:
            continue

    print("[-] Solver failed. Ensure challenge.json is in the same directory.")

if __name__ == "__main__":
    solve()
