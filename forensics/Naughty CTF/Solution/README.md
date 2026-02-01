# Solution to Naughty List

The given PCAP file was analysed and it was observed that data was exfiltrated using **TFTP**.

Two files were identified during the transfer:
- `naughty_list.db.enc`
- `ktmp`

The encrypted database was decrypted using the key file.  
The encryption consisted of an XOR operation followed by AES decryption.

A Python script was used to reconstruct the original SQLite database.

Flag: **LNMHACKS{f0r3n51c_m4lw4r3}**
