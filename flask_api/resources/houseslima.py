from flask.views import MethodView
from flask_smorest import abort, blueprint
from resources.schema import UpdateHouseSchema, HousesSchema
from models import HouseslimaModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = blueprint("Houseslima", __name__, description="Operations on Houseslima")

# Methods for the API's endpoint/s

@blp.route("/properties")
class Allproperties(MethodView):

    # Get all data
    @blp.response(200, HousesSchema(many=True))
    def get(self):
        return HouseslimaModel.query.all()


@blp.route("/properties/<int:id>")
class property(MethodView):

    # Get specific property by id
    @blp.response(200, HousesSchema)
    def get(self, id):
        
        property = HouseslimaModel.query.get_or_404(id)
        return property