from flask import *
from main import static_select

app = Flask(__name__)

@app.route("/project-catamere")
def home():
    return render_template("home.html")

@app.route("/project-catamere/static-gen")
def static_gen():
    message = static_select()
    print(message)
    return render_template("static.html", message=message)

# to avoid having to include port in url, look into reverse proxy server
# URL(s):
# PC Main page: http://clorox-flask.duckdns.org:5000/project-catamere
# PC Static gen: http://clorox-flask.duckdns.org:5000/project-catamere/static-gen