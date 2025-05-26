from flask import Flask, render_template_string, request, redirect, session, url_for
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
app.secret_key = 'ABCD11'

levels = {
    1: {
        'title': 'Nivel 1: Variables y tipos de datos',
        'description': 'Variables y tipos de datos en C++',
        'resources': [
            {'title': 'Programación en C++ 📗 variables y tipos de datos con c++', 'url': 'https://www.youtube.com/watch?v=YVlg0fC9Qgc&list=PLg9145ptuAigXfaTYcEdkmT6bmzZgEP9p&index=3'},
        ],
        'question': {
            'q': '¿Qué es una variable en C++ y tipos de datos más usados?',
            'options': ['Un valor de alguna clave, rest', 'Contenedor para almacenar datos, int', 'Tipo de dato cambiante, mult', 'Sirve para llamar funciones, var'],
            'answer': 'Contenedor para almacenar datos, int'
        }
    },
    2: {
        'title': 'Nivel 2: Primer programa',
        'description': 'Realizaremos un primer programa',
        'resources': [
            {'title': 'Programación en C++ 📗 nuestro primer programa', 'url': 'https://www.youtube.com/watch?v=Tpl1IPaUO-I&list=PLg9145ptuAigXfaTYcEdkmT6bmzZgEP9p&index=4'}
        ],
        'question': {
            'q': '¿Qué sintaxis de C++ es correcta?',
            'options': ['#include <iostream>, using namespace std; int main (){cout<<hola, return 0;}', 'using namespace std; int main (){cout<<hola', '#include <iostream>, using namespace std;'],
            'answer': '#include <iostream>, using namespace std; int main (){cout<<hola, return 0;}'
        }
    },
    3: {
        'title': 'Nivel 3: Operadores',
        'description': 'Veamos operadores en C++',
        'resources': [
            {'title': 'Programación en C++ 📗 OPERADORES (+ ejercicios)', 'url': 'https://www.youtube.com/watch?v=h-haeLsWM3U&list=PLg9145ptuAigXfaTYcEdkmT6bmzZgEP9p&index=5'}
        ],
        'question': {
            'q': '¿Qué operador me da 10, con la sintaxis correcta?',
            'options': ['int main (){int a=2, b=5; int suma; suma = a + b; cout << "resultado:"<< suma}', 'int main (){int a=4, b=3; int suma; suma = a * b; cout << "resultado:"<< suma}', 'int main (){int a=4, b=6; int suma; suma = a + b; cout << "resultado:"<< suma}'],
            'answer': 'int main (){int a=4, b=6; int suma; suma = a + b; cout << "resultado:"<< suma}'
        }
    }
}

MAX_LEVEL = len(levels)

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
            <h2>Introducción a C++</h2>
            <p>Bienvenido a este curso basico. C++ es un lenguaje de programación muy bueno y eficiente. Aquí profundizaremos un poco en conceptos fundamentales sobre el lenguaje.</p>
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
        <h2 style="color: white;">Práctica Básica de C++</h2>
        <form method="post">
            <div class="question">
                <p><strong>1. ¿Qué salida produce el siguiente código?</strong></p>
                <pre style="color:#ccc;">int x = 5;\ncout << x + 3;</pre>
                <label><input type="radio" name="q1" value="8"> 8</label><br>
                <label><input type="radio" name="q1" value="53"> 53</label><br>
                <label><input type="radio" name="q1" value="Error"> Error</label><br>
            </div>
            <div class="question">
                <p><strong>2. ¿Cuál es la instrucción correcta para mostrar texto?</strong></p>
                <label><input type="radio" name="q2" value="cout << 'Hola';"> cout << 'Hola';</label><br>
                <label><input type="radio" name="q2" value="print('Hola');"> print('Hola');</label><br>
                <label><input type="radio" name="q2" value="System.out.println('Hola');"> System.out.println('Hola');</label><br>
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
            <h2>Introducción a C++</h2>
            <p>C++ es un lenguaje de programación de propósito general que ofrece control de bajo nivel y abstracción de alto nivel. Es ampliamente utilizado en el desarrollo de sistemas, aplicaciones de alto rendimiento y videojuegos. En este curso, aprenderás desde los conceptos básicos de variables, tipos de datos, sintaxis de tu primer programa, hasta operadores y más.</p>
        </div>
        <h2 style="color: white;">¡Bienvenido!</h2>
        <p style="color: white;">Este curso interactivo te enseñará desde lo más básico hasta fundamentos de la programación en C++.</p>
        <a href="{{ url_for('start') }}"><button>Comenzar Curso</button></a>
    {% endif %}
</div>
</body>
</html>
"""

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
        return render_template_string(TEMPLATE, title="Curso C++", level=level, progress=progress, message=message, practice=None, result=None)
    elif level_num > MAX_LEVEL:
        return redirect(url_for('practice'))
    return render_template_string(TEMPLATE, title="Curso C++", level=None, progress=0, message=None, practice=None, result=None)

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
        if request.form.get('q2') == "cout << 'Hola';":
            score += 1
        result = f'Tu puntaje: {score}/2'
    return render_template_string(TEMPLATE, title="Práctica C++", level=None, practice=True, result=result, progress=100, message=None)


if __name__ == '__main__':
    app.run(debug=False, port=5000)