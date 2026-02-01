import socket

HOST = "0.0.0.0"
PORT = 5075

FLAG = "LNMHACKS{cryp70_3ncryp710n_d0n3}"
EXPECTED = "crypto_is_fun"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        with conn:
            conn.sendall(b"=== LNMHACKS CRYPTO CHALLENGE ===\n\n")

            with open("challenge.txt", "rb") as f:
                conn.sendall(f.read())

            conn.sendall(b"\n\nEnter decrypted plaintext: ")
            user_input = conn.recv(1024).strip().decode()

            if user_input == EXPECTED:
                conn.sendall(b"\nCorrect!\n")
                conn.sendall(FLAG.encode() + b"\n")
            else:
                conn.sendall(b"\nWrong answer. Try again later.\n")
