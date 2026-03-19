import socket
import threading

# Puertos que suelen dar información útil
TARGET_PORTS = [21, 22, 80, 443, 445, 5000, 8000, 8080]
TIMEOUT = 0.6

def obtener_banner(sock):
    """Intenta leer la presentación del servicio"""
    try:
        return sock.recv(1024).decode().strip()
    except:
        return "No revela banner"

def scan_ip(ip):
    for port in TARGET_PORTS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                banner = obtener_banner(sock)
                print(f"[!] {ip} -> Puerto {port} ABIERTO | Info: {banner}")
            sock.close()
        except:
            pass

def main():
    # Obtener IP local de forma inteligente
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








