from flask import Flask
from flask_smorest import Api


# Import blueprints for various resources
from app.blueprint.user_blueprint import user_blp
from app.blueprint.restaurant_blueprint import restaurant_blp
from app.blueprint.reservation_blueprint import reservation_blp
from app.blueprint.table_number_blueprint import table_blp
from app.blueprint.user_info_blueprint import user_info_blp
from app.blueprint.feedback_blueprint import feedback_blp
from app.extension import db, migrate
from config import Config

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Load configuration settings from Config class
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize the API (using Flask-Smorest for OpenAPI/Swagger)
    api = Api(app)

    # Register blueprints for various routes
    api.register_blueprint(user_blp)
    api.register_blueprint(restaurant_blp)
    api.register_blueprint(reservation_blp)
    api.register_blueprint(table_blp)
    api.register_blueprint(user_info_blp)
    api.register_blueprint(feedback_blp)

    # Simple route to confirm the app is running
    @app.route('/')
    def home():
        return "Welcome to the Restaurant API!"

    return app
