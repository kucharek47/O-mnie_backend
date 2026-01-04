import json
import os
from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS

dane_json = 'dane.json'

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)