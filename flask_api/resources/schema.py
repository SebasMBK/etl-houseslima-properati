from marshmallow import Schema, fields

"""
Houses
"""

class HousesSchema(Schema):
    id = fields.Int(required=True)
    type = fields.Str(required=True)
    score = fields.Float(dump_only=True)
    title = fields.Str(required=True)
    bedrooms = fields.Int(required=True)
    bathrooms = fields.Int(required=True)
    price = fields.Int(required=True)
    surface = fields.Int(required=True)
    district = fields.Str(required=True)
    geo_lon = fields.Float(required=True)
    geo_lat = fields.Float(required=True)
    place_lon = fields.Float(required=True)
    place_lat = fields.Float(required=True)
