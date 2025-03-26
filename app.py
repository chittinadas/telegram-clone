from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret")
socketio = SocketIO(app)

# রুটস
@app.route("/")
def home():
    return render_template("index.html")  # templates/index.html থেকে লোড করবে

# WebSocket ইভেন্টস
@socketio.on("message")
def handle_message(msg):
    print(f"মেসেজ পেয়েছি: {msg}")
    socketio.emit("response", {"user": "Server", "text": msg})

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0")