from flask import Flask, render_template
from flask_socketio import SocketIO, send 

app = Flask(__name__)
app.config["SECRET"] = "ajuianfa78fh9f78shfs768fgs7f6"
app.config["DEBUG"] = True
socketio = SocketIO(app, cors_aLLowed_origins="")

# Funcionalidade de enviar mensangem
@socketio.on("message")

def gerenciar_mensagem(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)
# criar a nossa 1ª página = 1ª rota
@app.route("/")
def home():
    return  render_template("index.html")
# roda o nosso
if __name__ == "__main__":  
    socketio.run(app, host=" 192.168.15.1")

# websocket -. tunel
