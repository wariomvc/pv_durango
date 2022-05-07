import os
from  werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash


from .dbsql import get_db


bpadmin = Blueprint('admin', __name__, url_prefix='/admin')
upload_folder = join(dirname(realpath(__file__)), "static\galeria")
extensiones_permitidas = ['jpeg','jpg','png']

def get_galeria_by_id(id_propiedad):
    db = get_db()
    imagenes_propiedad = db.execute('SELECT * FROM imagenes WHERE id_propiedad = ?',(id_propiedad,)).fetchall()   
    
    return imagenes_propiedad

@bpadmin.route('/delpic')
def delpic():
    pass

@bpadmin.route('/')
def registrar():
    db = get_db()
    propiedades = db.execute('SELECT id,whq, nombre, titulo, direccion FROM propiedades;').fetchall()
    
    print(propiedades)
    return render_template('admin/index.html', propiedades=propiedades)

def check_extensiones(filename=''):
    return '.' in filename and filename.rsplit('.')[1] in extensiones_permitidas

@bpadmin.route('/galeria/<id>',methods=('GET','POST'))
def galeria(id):
    imagenes_propiedad = get_galeria_by_id(id)
    if request.method == 'POST':
        id_propiedad = request.form['id_propiedad']
        titulo = request.form['titulo']
        info = request.form['descripcion']
        print(request.files)
        file = request.files['filename']
        if check_extensiones(filename=file.filename):         
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder,filename))
            print(upload_folder)
            db = get_db()
            db.execute("INSERT INTO imagenes (id_propiedad, URL,titulo, info) VALUES(?,?,?,?)",(id_propiedad,filename,titulo,info))
            db.commit() 
            
            print("Base de Datos Cerrada")
        else:
            flash("Tipo de Archivo no soportado")
        return render_template('admin/galeria.html', id=id, datos_imagenes=imagenes_propiedad)
    if request.method == 'GET':
        #imagenes_propiedad = get_galeria_by_id(id)
        if imagenes_propiedad != None:
            return render_template('admin/galeria.html', id=id, datos_imagenes=imagenes_propiedad)
        else:
            return render_template('admin/galeria.html', id=id, datos_imagenes=[])

@bpadmin.route('/addpic',methods=('GET','POST'))
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

@bpadmin.route('/registrar', methods=('GET','POST'))
def nueva_propiedad():
    if request.method == 'POST':
        whq = request.form['whq']
        nombre = request.form['nombre']
        titulo = request.form['titulo']
        frase = request.form['frase']
        direccion = request.form['direccion']
        estado = request.form['estado']
        doctmp = request.form['documentos']
        servtmp = request.form['servicios']
        medidastmp = request.form['medidas']
        consttmp = request.form['construccion']
        lugares = request.form['lugares']
        latitud = request.form['latitud']
        longitud = request.form['longitud']
        db = get_db()
        try:
            db.execute("""INSERT INTO 
                    propiedades
                    (whq,nombre,titulo,frase,direccion,estado,documentos,servicios,medidas,construccion,lugares,latitud,longitud)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) """, 
                    (whq,nombre,titulo,frase,direccion,estado, doctmp,servtmp,medidastmp,consttmp,lugares,latitud,longitud))
            db.commit()
        except db.IntegrityError as err:
            errores = "Error: "+ str(err)
            
        else:
            errores ="Agregado Exitosamente"
        flash(errores)
        return render_template('admin/registrar.html')
    else:
        return render_template('admin/registrar.html')

