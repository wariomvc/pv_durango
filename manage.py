from socket import if_nametoindex
import os
from app.app import app
if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = os.path.join(
    app.instance_path, '/static/galeria')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.run(debug=True)