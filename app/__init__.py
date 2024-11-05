from flask import Flask
from .db import db, migrate
from .models import book
from .routes.book_routes import books_bp
from .routes.author_routes import bp as authors_bp
import os


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    
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