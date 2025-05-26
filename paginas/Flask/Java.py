#Importamos las librerias necesarias
from flask import Flask, render_template_string, request, redirect, session, url_for
from flask_cors import CORS 


#Realizamos la conexion con el streamlib para poder llamarlo en la pagina
app = Flask(__name__)
CORS(app)
app.secret_key = 'ABCD11'


#Realizamos las preguntas con sus respuestas
levels = {
    1: {
        'title': 'Nivel 1: Variables y tipos de datos',
        'description': 'Aprenderás sobre variables y tipos de datos en Java.',
        'resources': [
            {'title': 'Variables y Tipos de Datos en Java | Curso Básico', 'url': 'https://www.youtube.com/watch?v=jjyuEyN7-Jg'},
        ],
        'question': {
            'q': '¿Cuál es un tipo de dato en Java?',
            'options': ['String', 'Numero', 'Texto', 'Variable'],
            'answer': 'String'
        }
    },
    2: {
        'title': 'Nivel 2: Primer programa',
        'description': 'Veamos los ciclos',
        'resources': [
            {'title': 'Tipos de ciclos en Java | Primeros ciclos', 'url': 'https://www.youtube.com/watch?v=legmXG1ntS4'}
        ],
        'question': {
            'q': '¿Para qué sirve el ciclo for en Java?',
            'options': ['Sirve para crear un ciclo para leer datos', 'Sirve para crear una funcion', 'Sirve para crear un ciclo hasta un limite en concreto'],
            'answer': 'Sirve para crear un ciclo hasta un limite en concreto'
        }
    },
    3: {
        'title': 'Nivel 3: Operadores',
        'description': 'Veamos los operadores en Java.',
        'resources': [
            {'title': 'Curso de Java - Operadores | Variables', 'url': 'https://www.youtube.com/watch?v=4OqOz8TYH1M'}
        ],
        'question': {
            'q': '¿Qué representa el operador % en Java?',
            'options': ['Suma', 'Resta', 'Residuo'],
            'answer': 'Residuo'
        }
    }
}

MAX_LEVEL = len(levels)


#Realizamos el quiz final incluyendo un lenguaje html y css para la interfaz
TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body {
            background-color: #2c2c2c;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #3a3a3a;
            padding: 30px;
            border-radius: 10px;
        }
        h1, h2 {
            color: #00ff99;
        }
        a {
            color: #66ccff;
        }
        .progress {
            width: 100%;
            background-color: #555;
            border-radius: 20px;
            margin-bottom: 20px;
        }
        .progress-bar {
            height: 20px;
            background-color: #00ff00;
            width: {{ progress }}%;
            border-radius: 20px;
        }
        .question {
            margin-top: 20px;
        }
        button {
            background-color: #007acc;
            color: white;
            border: none;
            padding: 10px 20px;
            margin-top: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background-color: #005f99;
        }
        .intro {
            background-color: #444;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>{{ title }}</h1>
    {% if level %}
        <div class="intro">
            <h2>Introducción a Java</h2>
            <p>Bienvenido a este curso básico. Java es un lenguaje de programación versátil y eficiente. Aquí aprenderás conceptos fundamentales.</p>
        </div>
        <div class="progress"><div class="progress-bar"></div></div>
        <h2>{{ level['title'] }}</h2>
        <p>{{ level['description'] }}</p>
        <ul>
        {% for res in level['resources'] %}
            <li><a href="{{ res['url'] }}" target="_blank">{{ res['title'] }}</a></li>
        {% endfor %}
        </ul>
        <form method="post">
            <div class="question">
                <p><strong>{{ level['question']['q'] }}</strong></p>
                {% for opt in level['question']['options'] %}
                    <label><input type="radio" name="answer" value="{{ opt }}"> {{ opt }}</label><br>
                {% endfor %}
            </div>
            <button type="submit">Enviar Respuesta</button>
        </form>
        {% if message %}
            <p><strong>{{ message }}</strong></p>
        {% endif %}
        <div style="margin-top:20px;">
            <a href="{{ url_for('start') }}"><button>Volver al inicio</button></a>
        </div>
    {% elif practice %}
        <h2 style="color: white;">Práctica Básica de Java</h2>
        <form method="post">
            <div class="question">
                <p><strong>1. ¿Qué salida produce el siguiente código?</strong></p>
                <pre style="color:#ccc;">int x = 5;\nSystem.out.println(x + 3);</pre>
                <label><input type="radio" name="q1" value="8"> 8</label><br>
                <label><input type="radio" name="q1" value="53"> 53</label><br>
                <label><input type="radio" name="q1" value="Error"> Error</label><br>
            </div>
            <div class="question">
                <p><strong>2. ¿Cuál es la instrucción correcta para mostrar texto en Java?</strong></p>
                <label><input type="radio" name="q2" value="System.out.println('Hola');"> System.out.println('Hola');</label><br>
                <label><input type="radio" name="q2" value="print('Hola');"> print('Hola');</label><br>
                <label><input type="radio" name="q2" value="Console.WriteLine('Hola');"> Console.WriteLine('Hola');</label><br>
            </div>
            <button type="submit">Verificar Respuestas</button>
        </form>
        {% if result %}
            <p><strong>{{ result }}</strong></p>
        {% endif %}
        <div style="margin-top:20px;">
            <a href="{{ url_for('start') }}"><button>Volver al inicio</button></a>
        </div>
    {% else %}
        <div class="intro">
            <h2>Introducción a Java</h2>
            <p>Java es un lenguaje de programación de propósito general, ampliamente utilizado en aplicaciones web, móviles y empresariales. En este curso, aprenderás desde los conceptos básicos hasta estructuras fundamentales del lenguaje.</p>
        </div>
        <h2 style="color: white;">¡Bienvenido!</h2>
        <p style="color: white;">Este curso interactivo te enseñará los fundamentos de la programación en Java.</p>
        <a href="{{ url_for('start') }}"><button>Comenzar Curso</button></a>
    {% endif %}
</div>
</body>
</html>
"""
#Este es como el backend del quiz final donde verificaremos que las respuestas esten correctas y dar el puntaje correspondiente
@app.route('/', methods=['GET', 'POST'])
def index():
    level_num = session.get('level', 0)
    message = ''
    if level_num > 0 and level_num <= MAX_LEVEL:
        level = levels[level_num]
        if request.method == 'POST':
            user_answer = request.form.get('answer')
            if user_answer == level['question']['answer']:
                session['level'] = level_num + 1
                return redirect(url_for('index'))
            else:
                message = '❌ Respuesta incorrecta. Intenta nuevamente.'
        progress = int((level_num - 1) / MAX_LEVEL * 100)
        return render_template_string(TEMPLATE, title="Curso Java", level=level, progress=progress, message=message, practice=None, result=None)
    elif level_num > MAX_LEVEL:
        return redirect(url_for('practice'))
    return render_template_string(TEMPLATE, title="Curso Java", level=None, progress=0, message=None, practice=None, result=None)

@app.route('/start')
def start():
    session['level'] = 1
    return redirect(url_for('index'))

@app.route('/practice', methods=['GET', 'POST'])
def practice():
    result = ''
    if request.method == 'POST':
        score = 0
        if request.form.get('q1') == '8':
            score += 1
        if request.form.get('q2') == "System.out.println('Hola');":
            score += 1
        result = f'Tu puntaje: {score}/2'
    return render_template_string(TEMPLATE, title="Práctica Java", level=None, practice=True, result=result, progress=100, message=None)

#Con esto ejecutamos el archivo Flask en el puerto elegido
if __name__ == '__main__':
    app.run(debug=False, port=5050)