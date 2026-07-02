<<<<<<< HEAD
from flask import window
first system 
app = Flask(__name__)
second
second system

app.route("/")
def hello():
    return "updated Flask sample application on azure hghapp service updated version-6"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
