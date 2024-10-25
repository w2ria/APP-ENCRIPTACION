from flask import Flask, request, render_template
from services.cifrado_desplazamiento_puro import procesar_cifrado_desplazamiento_puro
from services.algoritmo_de_vernam import procesar_algoritmo_de_vernam
from services.cifrado_transposicion_serie import procesar_transposicion_serie

app = Flask(__name__)
@app.route('/')
def principal():
    programasEncriptadores = ("Cifrado Desplazamiento Puro", "Algoritmo de Vernam", "Transposición por serie", "encriptador 4","encriptador 5") 
    programasDesncriptadores = ("desencriptador 1", "desencriptador 2", "desencriptador 3", "desencriptador 4","desencriptador 5")
    return render_template('index.html', encrip=programasEncriptadores, desencrip=programasDesncriptadores)


# @app.route('/lenguajes')
# def mostrarLenguajes():
#     misLenguajes = ("PHP", "Python", "Java", "C#",
#                     "JavaScript", "Perl", "Ruby", "Rust")
#     return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/cifrado-desplazamiento-puro', methods=['GET', 'POST'])
def cifrado_desplazamiento_puro():
    resultado = None
    
    if request.method == 'POST':
        texto = request.form.get('textoEncriptar')
        n = int(request.form.get('valorN') or 27)
        desplazamiento = int(request.form.get('desplazamiento') or 15)
        ecuacion = request.form.get('ecuacion')

        resultado = procesar_cifrado_desplazamiento_puro(texto, n, desplazamiento, ecuacion)
    
    return render_template('cifrado-desplazamiento-puro.html', resultado=resultado)


@app.route('/algoritmo-de-vernam', methods=['GET', 'POST'])
def algoritmo_de_vernam():
    resultado = None
    
    if request.method == 'POST':
        texto = request.form.get('texto')
        clave = request.form.get('clave')
        opcion = request.form.get('opcion')

        resultado = procesar_algoritmo_de_vernam(texto, clave, opcion)
    
    return render_template('algoritmo-de-vernam.html', resultado=resultado)


@app.route('/transposicion-serie', methods=['GET', 'POST'])
def cifrado_transposicion_serie():
    resultado = None
    texto_original = None
    
    if request.method == 'POST':
        texto = request.form.get('texto')

        texto_original, resultado = procesar_transposicion_serie(texto)
    
    return render_template('transposicion-serie.html', resultado=resultado, texto_original=texto_original)

if __name__ == '__main__':
    app.run(debug=True, port=5017)