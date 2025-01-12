from app import db

class Products(db.Model):
    __tablename__ = 'products'

    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255))
    id_user = db.Column(db.String(255), nullable=False)
    id_ecommerce = db.Column(db.Integer, db.ForeignKey('ecommerce.id_ecommerce'), nullable=False)

    price_histories = db.relationship('PriceHistory', backref='product', lazy=True)
    trackers = db.relationship('Tracker', backref='product', lazy=True)
