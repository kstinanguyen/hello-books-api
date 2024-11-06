from flask import Flask
from .db import db, migrate
from .models import book
from .routes.book_routes import bp as books_bp
from .routes.author_routes import bp as authors_bp
import os


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://kn_hello_books_api_db_user:ZKlpBrMUAGiM0GqjWdPnfR9UVlIxa9RN@dpg-cslfl9bqf0us738sg7u0-a.oregon-postgres.render.com/kn_hello_books_api_db'
    
    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)
    app.register_blueprint(authors_bp)

    return app