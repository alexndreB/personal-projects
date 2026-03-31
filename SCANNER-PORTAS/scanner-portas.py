import socket
import sys

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((host, port))
        if resultado == 0:
            print(f"Porta {port} ABERTA")
        sock.close()
    except:
        pass

if len(sys.argv) < 2:
    print("uso: python scanner.py <host>")
    print("exemplo: python scanner.py 192.168.1.8")
    sys.exit(1)

host = sys.argv[1]

for port in [22, 80, 443]:
    scan_port(host, port)
