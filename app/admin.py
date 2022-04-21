from distutils.command.config import config
import os
from asyncio.windows_events import NULL
import errno
import functools
from stat import FILE_ATTRIBUTE_NORMAL
from  werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


from .dbsql import get_db


bp = Blueprint('admin', __name__, url_prefix='/admin')
upload_folder = join(dirname(realpath(__file__)), "static\galeria")
extensiones_permitidas = ['jpeg','jpg','png']



@bp.route('/')
def registrar():
    db = get_db()
    propiedades = db.execute('SELECT id,whq, nombre, titulo, direccion FROM propiedades;').fetchall()
    print(propiedades)
    return render_template('admin/index.html', propiedades=propiedades)

def check_extensiones(filename=''):
    return '.' in filename and filename.rsplit('.')[1] in extensiones_permitidas

@bp.route('/galeria/<id>',methods=('GET','POST'))
def galeria(id):
    if request.method == 'POST':
        id_propiedad = request.form['id_propiedad']
        file = request.files['file']
        if check_extensiones(filename=file.filename):         
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder,filename))
            print(upload_folder)
            db = get_db()
            db.execute("INSERT INTO imagenes (id_propiedad, URL) VALUES(?,?)",(id_propiedad,filename))
            db.commit() 
            db.close()
            print("Base de Datos Cerrada")
        else:
            flash("Tipo de Archivo no soportado")
        return render_template('admin/galeria.html',id = id_propiedad)
    if request.method == 'GET':
        db = get_db()
        datos_imagenes = db.execute('SELECT * FROM imagenes WHERE id_propiedad = ?',(id,)).fetchall()   
        db.close()
        print(datos_imagenes)
        if datos_imagenes != None:
            return render_template('admin/galeria.html', id=id, datos_imagenes=datos_imagenes)
        else:
            return render_template('admin/galeria.html', id=id, datos_imagenes=[])

@bp.route('/addpic',methods=('GET','POST'))
def addpic():
    request.form['id']
    if request.method == 'POST':
        file = request.files['file']
        if check_extensiones(filename=file.filename):         
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder,filename))
            print(upload_folder)
        else:
            flash("Tipo de Archivo no soportado")
    return render_template('admin/galeria.html')

@bp.route('/registrar', methods=('GET','POST'))
def nueva_propiedad():
    if request.method == 'POST':
        whq = request.form['whq']
        nombre = request.form['nombre']
        titulo = request.form['titulo']
        frase = request.form['frase']
        direccion = request.form['direccion']
        doctmp = request.form['documentos']
        servtmp = request.form['servicios']
        medidastmp = request.form['medidas']
        consttmp = request.form['construccion']
        latitud = request.form['latitud']
        longitud = request.form['longitud']
        db = get_db()
        try:
            db.execute("""INSERT INTO 
                    propiedades (whq,nombre,titulo,frase,direccion,documentos,servicios,medidas,construccion,latitud,longitud)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?) """, 
                    (whq,nombre,titulo,frase,direccion, doctmp,servtmp,medidastmp,consttmp,latitud,longitud))
            db.commit()
        except db.IntegrityError:
            errores = "Hubo un error"
        else:
            errores ="Agregado Exitosamente"
        flash(errores)
        return render_template('admin/registrar.html')
    else:
        return render_template('admin/registrar.html')

