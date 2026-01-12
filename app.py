from flask import Flask
from routes.index import index_bp
from routes.add import add_bp
from routes.auth import auth_bp
app = Flask(__name__)
app.register_blueprint(index_bp, url_prefix="/api")
app.register_blueprint(add_bp, url_prefix="/api/add")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
