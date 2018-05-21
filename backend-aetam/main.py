from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    host = '0.0.0.0'
    port = '8000'
    app.run(debug=True, host=host, port=port)
