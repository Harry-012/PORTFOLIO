from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='')


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/<path:filename>')
def static_files(filename):
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    return 'Not Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
