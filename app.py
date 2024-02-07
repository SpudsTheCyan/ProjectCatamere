from flask import Flask, render_template, request, jsonify
from catamere_functions import static_select, dynamic_select, get_outcomes, update_outcomes
app = Flask(__name__)

@app.route('/project-catamere', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        match request.form['id']:
            case 'static' | 'dynamic':
                redirectUrl = request.form['redirecturl']
                return jsonify({'url': redirectUrl})
            case 'edit':
                outcomeStr = '\n'.join(get_outcomes())
                return jsonify({'database' : outcomeStr})
            case 'save':
                newOutcomes = (request.form['outcomefield']).split("\r\n")
                newOutcomesSplit = [*item.split(" ") for item in newOutcomes]
                if newOutcomesSplit % 2 == 0:
                  update_outcomes(newOutcomes)
                  return render_template('home.html')
                else:
                  flash('Invalid data!.', 'error')
                  return jsonify({'status': 'error', 'message': 'Invalid data!'})
            case _:
                return render_template('home.html')
    else:
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

if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="0.0.0.0", "port":8080)
    pass

# to avoid having to include port in url, look into reverse proxy server or SRV records

# URL(s):
# PC Main page:     http://clorox-flask.duckdns.org:5000/project-catamere
#                   http://192.168.1.98:5000/project-catamere
# PC Static gen:    http://clorox-flask.duckdns.org:5000/project-catamere/static-gen
#                   http://192.168.1.98:5000/project-catamere/static-gen
# PC Dynamic gen:   http://clorox-flask.duckdns.org:5000/project-catamere/dynamic-gen
#                   http://192.168.1.98:5000/project-catamere/dynamic-gen
