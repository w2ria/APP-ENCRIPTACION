# services/cifrado_desplazamiento_puro.py

def procesar_cifrado_desplazamiento_puro(texto, n, desplazamiento, ecuacion):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    resultado = ""
    longitud_alfabeto = len(alfabeto)
    texto_original = texto
    texto = texto.lower().replace(" ", "")
    

    for char in texto:
        # Normalizar caracteres con tilde
        if char in 'áàä':
            char = 'a'
        elif char in 'éèë':
            char = 'e'
        elif char in 'íìï':
            char = 'i'
        elif char in 'óòö':
            char = 'o'
        elif char in 'úùü':
            char = 'u'
        
        # Solo procesar caracteres que estén en el alfabeto
        if char in alfabeto:
            Mi = alfabeto.index(char)  # Encuentra el índice de la letra original
            
            if ecuacion == "CP1":  # Ci = (Mi + b) mod n
                Ci = (Mi + desplazamiento) % longitud_alfabeto
            elif ecuacion == "CP2":  # Mi = (Ci - b) mod n
                Ci = (Mi - desplazamiento) % longitud_alfabeto
            elif ecuacion == "CP3":  # Mi = (Ci + n - b) mod n
                Ci = (Mi + longitud_alfabeto - desplazamiento) % longitud_alfabeto
            else:
                return "Ecuación no válida"
            
            # Agregar el carácter encriptado al resultado
            resultado += alfabeto[Ci].upper()  # Convertir cada carácter encriptado a mayúsculas

    # Construir el mensaje final
    if ecuacion == "CP1":
        mensaje_final = f"La frase '{texto_original}' encriptada usando la ecuación {ecuacion} con n = {n} y b = {desplazamiento} es: '{resultado}'."
    else:
        mensaje_final = f"La frase '{texto_original}' desencriptada usando la ecuación {ecuacion} con n = {n} y b = {desplazamiento} es: '{resultado}'."
    
    return mensaje_final
