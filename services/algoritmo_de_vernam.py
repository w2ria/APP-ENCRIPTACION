# services/algoritmo_de_vernam.py

def procesar_algoritmo_de_vernam(texto, clave, opcion):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz 0123456789'

    # Normalizar texto y clave eliminando tildes y convirtiendo a minúsculas
    def normalizar(cadena):
        tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                  'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u'}
        return ''.join(tildes.get(c.lower(), c.lower()) for c in cadena)
        
    texto_original = texto
    texto = normalizar(texto)
    clave = normalizar(clave)
    
    # Obtener valores numéricos del alfabeto
    def obtener_valor(caracter):
        return alfabeto.index(caracter) if caracter in alfabeto else None

    # Igualar la longitud de la clave al texto
    while len(clave) < len(texto):
        clave += clave  # Repetir la clave si es más corta
    clave = clave[:len(texto)]  # Ajustar a la longitud exacta

    resultado = ""

    for i in range(len(texto)):
        valor_texto = obtener_valor(texto[i])
        valor_clave = obtener_valor(clave[i])

        if opcion == "ENC":
            valor_cifrado = (valor_texto + valor_clave) % 37
        else:
            valor_cifrado = (valor_texto + 37 - valor_clave) % 37

        caracter_cifrado = alfabeto[valor_cifrado]
        resultado += caracter_cifrado.upper()

    # Construir el mensaje final
    if opcion == "ENC":
        mensaje_final = f"La frase '{texto_original}' encriptada usando la clave '{clave}' es: '{resultado}'."
    else:
        mensaje_final = f"La frase '{texto_original}' desencriptada usando la clave '{clave}' es: '{resultado}'."
    
    return mensaje_final
