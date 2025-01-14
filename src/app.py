from flask import Flask, request, render_template
from extensions import db, migrate
from repositories.ecommerce_repository import EcommerceRepository

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializa las extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app

app = create_app()

from models import ecommerce, products, price_history, tracker

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        options = EcommerceRepository.get_all()
        print(options)
    elif request.method == 'POST':
        print(request.form)
        pass
    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)