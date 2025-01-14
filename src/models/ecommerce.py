from extensions import db

class Ecommerce(db.Model):
    __tablename__ = 'ecommerce'
    
    id_ecommerce = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    products = db.relationship('Products', backref='ecommerce', lazy=True)
