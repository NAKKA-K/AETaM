from flask import Flask

app = Flask(__name__)
app.config.from_object("aetam.settings.DevelopConfig")

from aetam import urls
from aetam import models
