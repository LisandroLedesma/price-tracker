from extensions import db

class PriceHistory(db.Model):
    __tablename__ = 'price_history'

    id_history = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id_product'), nullable=False)
    query_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    is_offer = db.Column(db.Boolean, nullable=False)
