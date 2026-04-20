from flask import Flask

def create_app():
    app = Flask(__name__)

    # import blueprint
    from app.routes.konsultasi_routes import konsultasi
    from app.routes.main_routes import main

    # register blueprint
    app.register_blueprint(konsultasi)
    app.register_blueprint(main)

    return app