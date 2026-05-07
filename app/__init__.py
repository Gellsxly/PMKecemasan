from flask import Flask

def create_app():
    app = Flask(__name__)

    # 🔐 WAJIB untuk session & flash
    app.secret_key = 'supersecretkey123'

    # import blueprint (rapikan di dalam function)
    from app.routes.auth_routes import auth
    from app.routes.admin_routes import admin
    from app.routes.konsultasi_routes import konsultasi
    from app.routes.main_routes import main

    # register blueprint
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(konsultasi)
    app.register_blueprint(main)

    return app