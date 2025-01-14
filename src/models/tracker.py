from extensions import db

class Tracker(db.Model):
    __tablename__ = 'tracker'

    id_tracker = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id_product'), nullable=False)
    execution_date = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
