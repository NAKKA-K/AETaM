from flask import Flask
from aetam import app

if __name__ == '__main__':
    host = '0.0.0.0'
    port = '8000'
    app.run(host=host, port=port)
