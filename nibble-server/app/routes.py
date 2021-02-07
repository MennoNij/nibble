from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/api/machine/v1/send-command", methods=["GET"])
def send_command():
  return "Send machine command"

