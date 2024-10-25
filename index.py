from flask import Flask, render_template

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


@app.route('/cifrado-desplazamiento-puro')
def contacto():
    return render_template('cifrado-desplazamiento-puro.html')


if __name__ == '__main__':
    app.run(debug=True, port=5017)