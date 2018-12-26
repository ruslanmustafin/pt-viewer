from flask import Flask, send_from_directory, render_template
import os
import glob
import json

app = Flask(__name__)

data_folder = '../data/'

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/textures/<path:path>')
def send_textures(path):
    return send_from_directory('textures', path)

@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('data', path)

@app.route("/")
def main():
    runs = sorted(glob.glob('data/*.json'))
    print(runs)
    # datasets = ["/data/data.json", "/data/data_2.json"]
    return render_template('index.html', datasets=json.dumps(runs))

app.run(host='0.0.0.0', port='8000')


