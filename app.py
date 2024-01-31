from flask import Flask, render_template, request, jsonify
from catamere_functions import static_select, dynamic_select
app = Flask(__name__)

@app.route('/project-catamere', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        redirectUrl = request.form['redirecturl']
        return jsonify({'url': redirectUrl})
    return render_template('home.html')

@app.route('/project-catamere/static-gen', methods=['GET','POST'])
def static_gen():
    if request.method == 'POST':
        return jsonify({'output': static_select()})
    return render_template('static.html')

@app.route('/project-catamere/dynamic-gen', methods=['GET','POST'])
def dynamic_gen():
    if request.method == 'POST':
        return jsonify({'output': dynamic_select()})
    return render_template('dynamic.html')

# to avoid having to include port in url, look into reverse proxy server

# URL(s):
# PC Main page:     http://clorox-flask.duckdns.org:5000/project-catamere
#                   http://192.168.1.98:5000/project-catamere
# PC Static gen:    http://clorox-flask.duckdns.org:5000/project-catamere/static-gen
#                   http://192.168.1.98:5000/project-catamere/static-gen
# PC Dynamic gen:   http://clorox-flask.duckdns.org:5000/project-catamere/dynamic-gen
#                   http://192.168.1.98:5000/project-catamere/dynamic-gen
