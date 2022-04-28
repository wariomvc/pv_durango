
import os
from pydoc import render_doc
import re

from flask import Flask, render_template, request

from .dbsql import get_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, '/static/galeria')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    from . import dbsql
    dbsql.init_app(app)

    from . import admin
    app.register_blueprint(admin.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/miubicacion')
    def miubicacion():
        return render_template('miubicacion.html')  

    def get_galeria_by_id(id_propiedad):
        db = get_db()
        imagenes_propiedad = db.execute('SELECT * FROM imagenes WHERE id_propiedad = ?',(id_propiedad,)).fetchall()   
        
        return imagenes_propiedad


    @app.route('/<int:id>/show')
    def showPropiedad(id):
        db = dbsql.get_db()
        #print(str(id))
        res = db.execute("SELECT * FROM propiedades WHERE id = ? ",(id,)).fetchone()
        imagenes_propiedad = get_galeria_by_id(id)
        #print(res['documentos'])
        return render_template('propiedad.html', p=res, datos_imagenes = imagenes_propiedad)
    
  
    return app

    