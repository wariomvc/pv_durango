from app.dbsql import *
from app.admin import bpadmin
import json
import os



from flask import Flask, render_template, request
#from importlib_metadata import method_cache

from app.dbsql import get_db
from app import app

# a simple page that says hello
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/miubicacion')
def miubicacion():
    return render_template('miubicacion.html')

def get_galeria_by_id(id_propiedad):
    db = get_db()
    imagenes_propiedad = db.execute('SELECT * FROM imagenes WHERE id_propiedad = ?', (id_propiedad,)).fetchall()

    return imagenes_propiedad

@app.route('/getubicaciones', methods=['POST'])
def getubicaciones():
    db = get_db()
    res = db.execute("SELECT * FROM propiedades").fetchall()
    db.close()
    resjson = json.dumps([dict(ix) for ix in res])
    # print(resjson)
    return resjson

@app.route('/getimagenes', methods=['POST'])
def getimagenes():
    db = get_db()
    r = db.execute('SELECT * FROM imagenes ').fetchall()
    imagenes_propiedad = json.dumps([dict(ix) for ix in r])
    db.close()
    return imagenes_propiedad

@app.route('/<int:id>/show')
def showPropiedad(id):
    db = get_db()
    # print(str(id))
    res = db.execute(
        "SELECT * FROM propiedades WHERE id = ? ", (id,)).fetchone()
    imagenes_propiedad = get_galeria_by_id(id)
    # print(res['documentos'])
    return render_template('propiedad.html', p=res, datos_imagenes=imagenes_propiedad)



    
init_app(app)

# create and configure the app

app.register_blueprint(bpadmin)



# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

