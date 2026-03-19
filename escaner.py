import socket
import threading

# Configuración
TARGET_PORTS = [21, 22, 80, 443, 445, 3306, 8080]
TIMEOUT = 0.5

def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f" [!] {ip}:{port} ABIERTO")
        sock.close()
    except:
        pass

def scan_ip(ip):
    # Escaneamos directamente sin filtros raros
    for port in TARGET_PORTS:
        check_port(ip, port)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_local = s.getsockname()[0]
    s.close()
    
    base_net = ".".join(ip_local.split('.')[:-1])
    print(f"--- Escaneando red: {base_net}.0/24 ---")
    
    threads = []
    for i in range(1, 255):
        ip = f"{base_net}.{i}"
        t = threading.Thread(target=scan_ip, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("\n--- Escaneo finalizado ---")

if __name__ == "__main__":
    main()









