from flask import Flask
from dotenv import load_dotenv
import os
from models.characters import Character, db
from models.user import userSchema
from flask_migrate import Migrate
from routes.endpoints import routes_blueprint
from subprocess import run
from flask_cors import CORS

# load environment varaibles from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    @app.cli.command("runserver")
    def run_server():
        # Run the scrapper.py to populate the database
        run_scraper()

        # Start the Flask development server
        app.run()

    @app.cli.command("runscrapper")
    def run_scraper():
        print("Running scrapper.py to populate the database...")
        from scrapper import scrape_and_save_chracters
        scrape_and_save_chracters()
        print("Scraping process completed.")

    app.register_blueprint(routes_blueprint)
    CORS(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()