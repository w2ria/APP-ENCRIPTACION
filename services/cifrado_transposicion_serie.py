# services/cifrado_transposicion_serie.py

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para determinar automáticamente MS1, MS2 y MS3
def obtener_series(longitud):
    ms1_pos, ms2_pos, ms3_pos = [], [], []
    
    for i in range(1, longitud + 1):
        if es_primo(i):
            ms1_pos.append(i)
        elif i % 2 == 0:
            ms2_pos.append(i)
        else:
            ms3_pos.append(i)
    
    return ms1_pos, ms2_pos, ms3_pos

def procesar_transposicion_serie(mensaje):
    # Eliminar espacios y poner en mayúsculas el mensaje
    mensaje = mensaje.replace(" ", "").upper().replace(",", "")
    
    # Obtener las posiciones de MS1, MS2 y MS3 según la longitud del mensaje
    ms1_pos, ms2_pos, ms3_pos = obtener_series(len(mensaje))
    
    # Listas para almacenar los caracteres de cada serie
    ms1, ms2, ms3 = [], [], []
    
    # Clasificar los caracteres según las posiciones
    for i in range(1, len(mensaje) + 1):
        if i in ms1_pos:
            ms1.append(mensaje[i - 1])
        elif i in ms2_pos:
            ms2.append(mensaje[i - 1])
        elif i in ms3_pos:
            ms3.append(mensaje[i - 1])
    
    # Concatenar las series en el orden MS1 + MS2 + MS3
    mensaje_cifrado = ''.join(ms1) + ''.join(ms2) + ''.join(ms3)
    
    return mensaje_cifrado
