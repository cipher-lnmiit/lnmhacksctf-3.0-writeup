# Solution to `Key in the Clear`

The packet capture file needs to be analysed using Wireshark or tshark.

The attack exploits an insecure file transfer protocol (TFTP) that transmits everything in plaintext:

1. **Open the PCAP in Wireshark**: Load `incident.pcap` and filter for TFTP traffic
2. **Extract transferred files**: Use Wireshark's "File → Export Objects → TFTP" to save all files
3. **Identify the files**: Three files are found:
   - `svc_update` - A Linux executable that references AES-256-ECB encryption
   - `.cache_01` - A 32-byte binary file (the encryption key!)
   - `backup_2024.bak` - Encrypted database file
4. **Extract the key**: The `.cache_01` file contains the AES-256 key transmitted in plaintext. Convert it to hex format using `xxd -p .cache_01 | tr -d '\n'`
5. **Decrypt the backup**: Use OpenSSL to decrypt: `openssl enc -aes-256-ecb -d -in backup_2024.bak -out decrypted.db -K <HEX_KEY> -nosalt`
6. **Extract the flag**: Open the decrypted SQLite database and query the data table to find the flag

The key vulnerability is transmitting the encryption key "in the clear" over an unencrypted protocol, rendering the encryption completely useless.

**Flag:** `LNMHACKS{pc4p_2_k3y_0wn3d}`