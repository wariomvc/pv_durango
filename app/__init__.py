from flask import Flask
import os

app = Flask(__name__, instance_relative_config=True)
app.config['UPLOAD_FOLDER'] = os.path.join(
app.instance_path, '/static/galeria')
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

from app import rutas