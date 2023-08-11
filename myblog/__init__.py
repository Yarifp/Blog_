from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sitios+123@localhost/mi_base_de_datos'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Cargar las configuraciones
from config import DevelopmentConfig
app.config.from_object('config.DevelopmentConfig')
#db = SQLAlchemy(app)

# Importar vistas
from myblog.views.auth import auth
from myblog.views.blog import blog

# Registrar blueprints
app.register_blueprint(auth)
app.register_blueprint(blog)
app.add_url_rule('/', endpoint='index')

# Colocar db.create_all() dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True ,port=5000,use_reloader=False)
