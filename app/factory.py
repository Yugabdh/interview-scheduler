import connexion
import dotenv

from flask.json import JSONEncoder
from flask_jwt_extended import JWTManager

from bson import json_util, ObjectId
from datetime import datetime


class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            print("here:", str(obj))
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    config = dotenv.dotenv_values(".env")

    connexion_app = connexion.App(__name__, specification_dir='../openapi/')
    connexion_app.add_api('swagger.yml', strict_validation=True, validate_responses=True)
    connexion_app.app.json_encoder = MongoJsonEncoder

    connexion_app.app.config["MONGO_URI"] = config['MONGO_URI']
    # Initialize JWT
    connexion_app.app.config['JWT_SECRET_KEY'] = '2c9787d18c25c845d4ac9b57492a573c5e3fde998e0d1db62443b516f1aa6a25'
    jwt = JWTManager()
    jwt.init_app(connexion_app.app)  # Register JWTManager with the Flask app

    print(connexion_app.app.config["MONGO_URI"])
    # Import blueprints
    from .api.v1.auth import auth_bp
    # Register blueprints
    connexion_app.app.register_blueprint(auth_bp)

    return connexion_app
