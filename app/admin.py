import errno
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .dbsql import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
def regitrar():
        return render_template('registrar.html')
    
@bp.route('/nuevo', methods=('GET','POST'))
def nueva_propiedad():
    if request.method == 'POST':
        whq = request.form['whq']
        nombre = request.form['nombre']
        titulo = request.form['titulo']
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
                    propiedades (whq,nombre,titulo,direccion,documentos,servicios,medidas,construccion,latitud,longitud)
                    VALUES (?,?,?,?,?,?,?,?,?,?) """, 
                    (whq,nombre,titulo,direccion, doctmp,servtmp,medidastmp,consttmp,latitud,longitud))
            db.commit()
        except db.IntegrityError:
            errores = "Hubo un error"
        else:
            errores ="Agregado Exitosamente"
        flash(errores)
        return render_template('registrar.html')
    else:
        return render_template('registrar.html')