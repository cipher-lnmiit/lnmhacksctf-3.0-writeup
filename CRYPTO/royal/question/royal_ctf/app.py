from flask import Flask, jsonify, request, render_template
from hashlib import sha256
import random
from ecdsa.ecdsa import generator_secp256k1, Public_key, Private_key, Signature

PORT = 4069
FLAG = "LNMHACKS{winter_is_com1ng_the_things_i_do_for_love}"

G = generator_secp256k1
n = G.order()

random.seed(1337)

def H(m):
    return int.from_bytes(sha256(m.encode()).digest(), "big")

d = random.randint(1, n - 1)
Q = d * G
pub = Public_key(G, Q)
priv = Private_key(pub, d)

k1 = random.randint(2, n - 2)
k2 = k1

messages = [
    ("ROYAL_NOTICE: Grain shipment approved.", k1),
    ("ROYAL_NOTICE: Rations delayed.", k2),
    ("ROYAL_NOTICE: Envoy cleared.", random.randint(2, n - 2))
]

store = []
for i, (msg, k) in enumerate(messages):
    sig = priv.sign(H(msg), k)
    store.append({
        "index": i,
        "message": msg,
        "r": hex(sig.r),
        "s": hex(sig.s)
    })

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/messages")
def messages_route():
    return jsonify({"messages": store})

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(force=True)
    r = int(data["r"], 16)
    s = int(data["s"], 16)
    msg = data["message"]
    sig = Signature(r, s)
    if not pub.verifies(H(msg), sig):
        return jsonify({"ok": False}), 403
    if msg.startswith("ROYAL_ORDER:"):
        return jsonify({"ok": True, "flag": FLAG})
    return jsonify({"ok": True})

if __name__ == "__main__":
    print("Starting vulnerable royal-sign server on port", PORT)
    app.run(host="0.0.0.0", port=PORT)