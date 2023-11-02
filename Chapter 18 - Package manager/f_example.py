from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "  YO AFIRMO QUE EL CLUB ATLÉTICO BOCA JUNIORS SERÁ EL CAMPEÓN DE LA COPA LIBERTADORES 2023 DIA 04 DE OCTUBRE DE 2023!  "

app.run(port='8000')                                                                         