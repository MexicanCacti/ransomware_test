import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
PORT = 6500

print("Your Computer Name is:" + hostname
      + "\nYour Computer IP Address is:" + IPAddr)
      
keyDict = {}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IPAddr, PORT))
    s.listen()
    s.settimeout(1.0)

    try:
        while True:
            try:
                conn, addr = s.accept()
                conn.settimeout(1.0)
            except socket.timeout:
                continue

            with conn:
                print('Connected by', addr)
                while True:
                    try:
                        data = conn.recv(1024)
                    except socket.timeout:
                        continue
                    
                    if not data:
                        break
                    
                    decodedData = data.decode()
                    hostname, key = decodedData.split('|')
                    print(f"{hostname} ({addr[0]}) sent key: {key}")
                    keyDict[addr[0]] = {
                        "hostname": hostname,
                        "key": key
                    }
    except KeyboardInterrupt:
        print("\nServer shutting down.")
