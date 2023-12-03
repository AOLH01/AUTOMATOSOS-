from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import ply.lex as lex
import ply.yacc as yacc

app = Flask(__name__)

def procesarCadena(entrada):
    # Implementa tu lógica para procesar la cadena de entrada
    # Para fines de demostración, asumamos que el procesamiento es convertir la cadena a mayúsculas
    cadenaProcesada = entrada.upper()
    return cadenaProcesada

def checkSintaxisCorrect(entrada):
    if entrada != "":
        return True
    return "Error de sintaxis"

def analyze_sentiments(entrada):
    sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
    resultado = sentiment_analyzer(entrada)[0]
    sentimiento = resultado['label']
    return sentimiento

# Definición de tokens
tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
)

# Expresiones regulares para los tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Definición de la regla para el token NUMERO
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Variables para almacenar caracteres no reconocidos y mensajes de error de sintaxis
caracteres_no_reconocidos = []

# Variable para controlar si se debe imprimir el resultado
imprimir_resultado = True

# Manejo de errores
def t_error(t):
    global caracteres_no_reconocidos
    global imprimir_resultado
    caracteres_no_reconocidos.append(t.value[0])
    imprimir_resultado = False
    t.lexer.skip(1)


# Reglas de gramática y precedencia para el analizador sintáctico
def p_expresion(p):
    """
    expresion : expresion SUMA expresion
              | expresion RESTA expresion
              | expresion MULTIPLICACION expresion
              | expresion DIVISION expresion
              | PARENTESIS_IZQ expresion PARENTESIS_DER
              | NUMERO
    """
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '(' and p[3] == ')':
        p[0] = p[2]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            if p[3] != 0:
                p[0] = p[1] / p[3]
            else:
                print("División por cero")
                p[0] = None

# Regla de error para errores sintácticos
def p_error(p):
    global imprimir_resultado
    imprimir_resultado = False

# Construir el lexer
lexer = lex.lex()

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Analizando léxicamente la expresión que se ingrese
def evaluar_lexico(expresion):
    # Reiniciar la lista antes de cada análisis
    global caracteres_no_reconocidos
    caracteres_no_reconocidos = []

    # Ejecutar el lexer
    lexer.input(expresion)

    # Iterar sobre los tokens
    for token in lexer:
        pass  # No es necesario hacer nada aquí

    # Crear cadena de caracteres no reconocidos separados por coma
    caracteres_concatenados = ",".join(map(str, caracteres_no_reconocidos))

    return caracteres_concatenados

@app.route("/", methods=["GET", 'POST'])
def homepage():
    mensaje_sentimiento = None

    if request.method == "POST":
        try:
            entrada = request.form.get("entrada")
            print("Entrada recibida:", entrada)


            # Sentimiento debe ser una cadena como "POSITIVE", "NEGATIVE" o "NEUTRAL"
            sentimiento = "NEUTRAL"

            # Mapeo de sentimientos a mensajes
            mensajes = {
                "POSITIVE": "La persona está feliz.",
                "NEGATIVE": "La persona está triste o enojada.",
                "NEUTRAL": "La persona tiene un sentimiento neutral."
            }

            # Seleccionar el mensaje basado en el sentimiento
            mensaje_sentimiento = mensajes.get(sentimiento, "Sentimiento desconocido")

            return mensaje_sentimiento

        except Exception as e:
            print("Error:", str(e))
            return "Error interno del servidor."

    return render_template("Menu.html", title="Lenguajes y Automatosos II", mensaje_sentimiento=mensaje_sentimiento)


@app.route("/lexico", methods=["GET", "POST"])
def lexico():
    if request.method == 'POST':
        # Cadena de entrada
        expresion = request.form['lexicalInput']
    else:
        expresion = ""

    caracteres_no_reconocidos = evaluar_lexico(expresion)

    # Retornar la cadena al renderizar la plantilla
    return render_template('pag3.html', caracteres_no_reconocidos=caracteres_no_reconocidos, expresion=expresion)


@app.route("/sintactico", methods=["GET"])
def sintactico():
    return render_template("pag2.html", title="Lenguajes y Automatosos II")

@app.route("/bikes", methods=["GET"])
def bikes():
    return render_template("Biker.html", title="Lenguajes y Automatosos II")

if __name__ == "__main__":
    app.run(debug=True)