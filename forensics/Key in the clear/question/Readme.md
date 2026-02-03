# Key in the Clear, 200 points

## Author: [KavyaTejpal](__https://github.com/KavyaTejpal__)

## Problem

During a routine security audit, administrators noticed unusual outbound traffic from an internal server shortly before it went offline. The system was believed to contain sensitive records scheduled for an encrypted backup.

Incident responders recovered a network capture from the time of the suspected breach. Initial analysis suggests that an attacker executed an unauthorized program, encrypted a database, and attempted to exfiltrate files using a lightweight file transfer protocol.

The server has since been wiped, and no other logs or files remain.

Your task is to analyze the captured network traffic, reconstruct what the attacker transferred, and determine what data was compromised.

A packet capture file `incident.pcap` is given.

## Producing it

The challenge is created by capturing a TFTP (Trivial File Transfer Protocol) session where an attacker exfiltrates three files: an executable (`svc_update`), an AES-256 encryption key (`.cache_01`), and an encrypted database (`backup_2024.bak`). The key vulnerability is that the encryption key is transmitted in plaintext over the insecure TFTP protocol, allowing complete decryption of the encrypted data.