from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from resources.schema import HousesSchema
from models import HouseslimaModel
from db import db

blp = Blueprint("Houseslima", __name__, description="Operations on Houseslima")

# Methods for the API's endpoint/s

@blp.route("/")
class Mainpage(MethodView):
    def get(self):
        return "Houseslima Project's API"

@blp.route("/properties")
class Allproperties(MethodView):

    # Get all data
    @blp.response(200, HousesSchema(many=True))
    def get(self):
        return HouseslimaModel.query.all()

    # Post data
    @blp.arguments(HousesSchema(many=True))
    @blp.response(200, HousesSchema(many=True))
    def post(self, new_property):
        properties = [HouseslimaModel(**record) for record in new_property ]

        if len(properties) > 100:
            abort(400, message="The transaction limit is of 100")
        
        for row in new_property:
            if HouseslimaModel.query.get(row['id']):
                abort(400, message=f'The property_id {row["id"]} already exists.')
        try:
            db.session.add_all(properties)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"{e}")
        
        return properties


@blp.route("/properties/<int:id>")
class property(MethodView):

    # Get specific property by id
    @blp.response(200, HousesSchema)
    def get(self, id):
        
        property = HouseslimaModel.query.get_or_404(id)
        return property