
class Config:
    DEBUG = True
    TESTING = True

    #Configuración de base dedatos 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:sitios+123@localhost/mi_base_de_datos"


class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:sitios+123@localhost/mi_base_de_datos"

