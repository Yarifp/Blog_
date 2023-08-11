from myblog import app, db  # Importa la aplicación Flask y la instancia de SQLAlchemy
app.debug = True

# ...
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

