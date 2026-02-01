from Cryptodome.Cipher import AES

KEY = open("ktmp","rb").read()
cipher = AES.new(KEY, AES.MODE_ECB)

data = open("naughty_list.db.enc","rb").read()
xor_dec = bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(data)])
plain = cipher.decrypt(xor_dec)

pad = plain[-1]
open("recovered.db","wb").write(plain[:-pad])
