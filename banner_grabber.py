def buscar_banner(ip, puerto):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, puerto))
        
        # Intento 1: Ver si el servidor habla solo (como SSH o FTP)
        try:
            banner = s.recv(1024)
            if banner:
                print(f"\n[+] Puerto {puerto} (Auto-Banner): {banner.decode().strip()}")
                s.close()
                return
        except:
            pass # Si no habla solo, intentamos provocarle

        # Intento 2: Provocar respuesta (para Web)
        s.send(b"HEAD / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
        respuesta = s.recv(1024)
        print(f"\n[+] Puerto {puerto} (Web-Banner):\n{respuesta.decode().strip()}")
        s.close()
    except:
        print(f"[-] Sin respuesta en puerto {puerto}")
