from flask import Flask, jsonify

app = Flask(__name__)

# Você muda aqui quando quiser bloquear ou liberar
STATUS_ATUAL = "OK"  # coloque "BLOQUEADO" quando quiser travar o sistema

@app.get("/verificar")
def verificar():
    return jsonify({"status": STATUS_ATUAL})

if __name__ == "__main__":
    app.run()
