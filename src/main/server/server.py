from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connection_handler
from src.main.routes.pessoa_fisica_routes import pf_route_bp
from src.main.routes.pessoa_juridica_routes import pj_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pf_route_bp)
app.register_blueprint(pj_route_bp)
