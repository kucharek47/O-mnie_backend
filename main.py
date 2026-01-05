import json
import os
from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

dane_json = 'dane.json'
app.json.sort_keys = False

@app.route('/api/dane', methods=['GET'])
def get_dane():
    if not os.path.exists(dane_json):
        return jsonify({"error": "Plik danych nie znaleziony"}), 404

    try:
        with open(dane_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Błąd serwera: {str(e)}"}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, port=13004)