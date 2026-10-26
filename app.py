import json, os
from flask import Flask, jsonify, render_template
from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *
from tv_ip import tvIP

app = Flask(__name__)
STORE_FILE = "tv_store.json"

# carrega a chave salva (se existir)
store = {}
if os.path.exists(STORE_FILE):
    with open(STORE_FILE) as f:
        store = json.load(f)

print("[APP]: Tentando conectar...")
client = WebOSClient(tvIP[0])   # ou secure=True se for TV nova
client.connect()
print("[APP]: Conectado!")
for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("Aceite a conexão na TV!")

# salva chave para nao pedir toda vez
with open(STORE_FILE, "w") as f:
    json.dump(store, f)

# Atalhos
media = MediaControl(client)
system = SystemControl(client)
app_control = ApplicationControl(client)
inp = InputControl(client)
inp.connect_input()

apps = app_control.list_apps()

def achar_app(nome):
    for a in apps:
        if nome in a["title"].lower():
            return a
    return None

# ROTAS - INTERFACE /////////

@app.route("/")
def index():
    print("[APP]: rota ROOT conectado!")
    return render_template("index.html")

# ROTAS - BOTOES ///////////

# VOLUME
@app.route("/api/volume/up", methods=["POST"])
def volume_up():
    print("[APP]: Volume UP conectado!")
    media.volume_up()
    return jsonify(ok=True)

@app.route("/api/volume/down", methods=["POST"])
def volume_down():
    print("[APP]: Volume DOWN conectado!")
    media.volume_down()
    return jsonify(ok=True)

@app.route("/api/volume/mute", methods=["POST"])
def mute():
    print("[APP]: Volume MUTE conectado!")
    estado = media.get_volume().get("muted", False)
    media.mute(not estado)
    return jsonify(ok=True)

# SETAS
@app.route("/api/setas/up", methods=["POST"])
def setas_up():
    print("[APP]: Seta UP conectado!")
    inp.up()
    return jsonify(ok=True)

@app.route("/api/setas/down", methods=["POST"])
def setas_down():
    print("[APP]: Seta DOWN conectado!")
    inp.down()
    return jsonify(ok=True)

@app.route("/api/setas/left", methods=["POST"])
def setas_left():
    print("[APP]: Seta LEFT conectado!")
    inp.left()
    return jsonify(ok=True)

@app.route("/api/setas/right", methods=["POST"])
def setas_right():
    print("[APP]: Seta RIGHT conectado!")
    inp.right()
    return jsonify(ok=True)

# APPS
@app.route("/api/apps/youtube", methods=["POST"])
def abrir_youtube():
    print("[APP]: App YOUTUBE conectado!")
    a = achar_app("youtube")
    if not a:
        return jsonify(ok=False, erro="YouTube não encontrado"), 404
    app_control.launch(a)
    return jsonify(ok=True)

@app.route("/api/apps/netflix", methods=["POST"])
def abrir_netflix():
    print("[APP]: App NETFLIX conectado!")
    a = achar_app("netflix")
    if not a:
        return jsonify(ok=False, erro="Netflix não encontrada"), 404
    app_control.launch(a)
    return jsonify(ok=True)

# ACOES
app.route("/api/acoes/type", methods=["POST"])
def test_digitar():
    inp.type("This sends keyboard input!")

@app.route("/api/acoes/off", methods=["POST"])
def power_off():
    system.power_off()
    return jsonify(ok=True)

@app.route("/api/acoes/ok", methods=["POST"])
def setas_ok():
    print("[APP]: Acao OK conectado!")
    inp.ok()
    return jsonify(ok=True)

@app.route("/api/acoes/home", methods=["POST"])
def setas_home():
    print("[APP]: Acao HOME conectado!")
    inp.home()
    return jsonify(ok=True)

@app.route("/api/acoes/back", methods=["POST"])
def setas_back():
    print("[APP]: Acao BACK conectado!")
    inp.back()
    return jsonify(ok=True)

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000, debug=False)
    app.run(debug=True)