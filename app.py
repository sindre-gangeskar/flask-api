from flask import Flask
from routes.index import index_bp
from routes.add import add_bp
from routes.subtract import subtract_bp
from routes.multiply import multiply_bp
from routes.auth import auth_bp
from routes.divide import divide_bp
from flasgger import Swagger

app = Flask(__name__)
swagger_template = {
    "info": {
        "title": "Sindre Gangeskar's simple Flask API documentation",
        "description": "**Documentation for all available API endpoints**.",
        "version": "1.0.0",
        "contact": {"name": "Sindre Gangeskar", "url": "https://sindregangeskar.dev"},
    }
}
swagger = Swagger(app, template=swagger_template)

app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(add_bp, url_prefix="/api/add")
app.register_blueprint(subtract_bp, url_prefix="/api/subtract")
app.register_blueprint(multiply_bp, url_prefix="/api/multiply")
app.register_blueprint(divide_bp, url_prefix="/api/divide")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
