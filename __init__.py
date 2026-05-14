from flask import Flask

from app.controller.record_ctrl import record_bp

from app.controller.export_ctrl import export_bp

from app.controller.log_ctrl import log_bp


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "mcs_secret"

    app.register_blueprint(record_bp)

    app.register_blueprint(export_bp)

    app.register_blueprint(log_bp)

    return app
