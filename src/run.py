from flask import Flask
from extensions import db, migrate
from views import main_bp 


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializa las extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(main_bp)
    return app

app = create_app()

from models import ecommerce, products, price_history, tracker    

if __name__ == '__main__':
    app.run(debug=True)