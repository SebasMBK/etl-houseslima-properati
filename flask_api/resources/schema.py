from marshmallow import Schema, fields

"""
Houses
"""

class HousesSchema(Schema):
    id = fields.Str(dump_only=True)
    type = fields.Str(dump_only=True)
    score = fields.Float(dump_only=True)
    title = fields.Str(dump_only=True)
    bedrooms = fields.Int(dump_only=True)
    bathrooms = fields.Int(dump_only=True)
    price = fields.Int(dump_only=True)
    surface = fields.Int(dump_only=True)
    district = fields.Str(dump_only=True)
    geo_lon = fields.Float(dump_only=True)
    geo_lat = fields.Float(dump_only=True)
    place_lon = fields.Float(dump_only=True)
    place_lat = fields.Float(dump_only=True)
