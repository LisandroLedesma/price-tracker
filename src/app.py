from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

app = Flask(__name__) 
app.config.from_object('config.Config') 
db = SQLAlchemy(app) 
migrate = Migrate(app, db)

from models import ecommerce, products, price_history, tracker

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)