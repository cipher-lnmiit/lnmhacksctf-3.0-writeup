import numpy as np
import json

class EasyLWE:
    def __init__(self):
        self.n = 64
        self.q = 257
        self.state = 42

    def get_error(self):
        # small bounded noise
        self.state = (self.state * 5 + 1) % 13
        return self.state - 6   # [-6, 6]

    def generate(self, flag):
        # 🔑 SMALL SECRET (key change)
        s = np.random.randint(-3, 4, size=self.n)

        m = len(flag) * 8
        A = np.random.randint(0, self.q, size=(m, self.n))

        # noise
        e = np.array([self.get_error() for _ in range(m)])

        # encode flag as bits → {0, 128}
        bits = "".join(format(ord(c), "08b") for c in flag)
        msg = np.array([int(b) * (self.q // 2) for b in bits])

        # LWE equation
        b = (A @ s + e + msg) % self.q

        return A.tolist(), b.tolist()


# ====== GENERATE CHALLENGE ======
flag = "LNMHACKS{L0G1C_BE4TS_L4TT1C3S}"

A_data, b_data = EasyLWE().generate(flag)

with open("challenge.json", "w") as f:
    json.dump(
        {
            "A": A_data,
            "b": b_data,
            "q": 257
        },
        f
    )

print("[+] Generated challenge.json")
print("[+] Flag:", flag)
