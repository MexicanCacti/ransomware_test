import socket
import sys
from pathlib import Path
import os

PORT = 6500
    
keyDict = {}

def main():
  if len(sys.argv) < 3:
    print("Usage: python ./keylistener.py <IP> <PORT>")
    sys.exit(1)
  IPAddr = sys.argv[1]
  PORT = int(sys.argv[2])
  print(f"Listening on IP: {IPAddr} Port: {PORT}")
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
      print("\nShutting down.")
           


if __name__ == "__main__":
    main()
