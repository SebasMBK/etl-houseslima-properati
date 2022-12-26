from db import db

class HouseslimaModel(db.Model):
    __tablename__ = "realstatedata"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    score = db.Column(db.Float(precision=7))
    title = db.Column(db.String(255))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    surface = db.Column(db.Integer)
    district = db.Column(db.String(100))
    geo_lon = db.Column(db.Float(precision=3))
    geo_lat = db.Column(db.Float(precision=3))
    place_lon = db.Column(db.Float(precision=3))
    place_lat = db.Column(db.Float(precision=3))