from flask import Flask, request, render_template
from services.cifrado_desplazamiento_puro import procesar_cifrado_desplazamiento_puro

app = Flask(__name__)
@app.route('/')
def principal():
    programasEncriptadores = ("Cifrado Desplazamiento Puro", "encriptador 2", "encriptador 3", "encriptador 4","encriptador 5") 
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


if __name__ == '__main__':
    app.run(debug=True, port=5017)