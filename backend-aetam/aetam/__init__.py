from flask import Flask

app = Flask(__name__)

from aetam import views
from aetam import urls

