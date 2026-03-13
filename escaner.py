from scapy.all import ARP, Ether, srp

def escanear_red(ip_rango):
    # Crear paquete ARP
    arp = ARP(pdst=ip_rango)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete = ether/arp
    
    # Enviar y recibir
    resultado = srp(paquete, timeout=3, verbose=0)[0]
    
    dispositivos = []
    for enviado, recibido in resultado:
        dispositivos.append({'ip': recibido.psrc, 'mac': recibido.hwsrc})
    return dispositivos

if __name__ == "__main__":
    # Cambia esto por tu rango de red (usualmente 192.168.1.0/24)
    rango = "192.168.1.0/24"
    print(f"Escaneando red: {rango}...")
    dispositivos = escanear_red(rango)
    
    for dev in dispositivos:
        print(f"IP: {dev['ip']} - MAC: {dev['mac']}")


