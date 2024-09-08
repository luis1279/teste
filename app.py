from flask import Flask, render_template, request
import random
from vercel_python import make_app

app = Flask(__name__)

numero_secreto = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    if request.method == "POST":
        try:
            palpite = int(request.form["palpite"])
            if palpite < numero_secreto:
                mensagem = "Tente um número maior!"
            elif palpite > numero_secreto:
                mensagem = "Tente um número menor!"
            else:
                mensagem = "Parabéns! Você acertou!"
        except ValueError:
            mensagem = "Por favor, insira um número válido."
    
    return render_template("index.html", mensagem=mensagem)

# Adicionar o adaptador para Vercel
app = make_app(app)

if __name__ == "__main__":
    app.run(debug=True)
