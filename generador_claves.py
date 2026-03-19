import itertools

def generar_diccionario():
    print("--- Creador de Diccionarios Pro ---")
    base = input("Palabra base (ej: nombre): ")
    anio = input("Año (ej: 2026): ")
    
    # Lista de variaciones: Palabra, Palabra con Mayúscula, Año y Símbolo
    elementos = [base, base.capitalize(), anio, "!"]
    
    # Generamos combinaciones de 3 elementos (ej: Nombre + Año + !)
    combinaciones = list(itertools.permutations(elementos, 3))

    with open("diccionario.txt", "w") as f:
        for combo in combinaciones:
            # Une los trozos y los guarda en el archivo
            f.write("".join(combo) + "\n")
    
    print(f"\n[+] Éxito: Se han guardado {len(combinaciones)} claves en 'diccionario.txt'")

if __name__ == "__main__":
    generar_diccionario()
