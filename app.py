from flask import Flask, render_template, request

app = Flask(__name__)

# Función para verificar si un número tiene dígitos repetidos
def tiene_digitos_repetidos(numero):
    return len(set(str(numero))) < len(str(numero))

@app.route('/', methods=['GET', 'POST'])
def index():
    numeros_repetidos = []
    numeros_sin_repetidos = []

    if request.method == 'POST':
        numeros = request.form['numeros']
        lista_numeros = numeros.splitlines()

        for numero in lista_numeros:
            numero = numero.strip()
            if tiene_digitos_repetidos(numero):
                numeros_repetidos.append(numero)
            else:
                numeros_sin_repetidos.append(numero)

    return render_template('index.html', numeros_repetidos=numeros_repetidos, numeros_sin_repetidos=numeros_sin_repetidos)

if __name__ == '__main__':
    app.run(debug=True)
