from flask import Flask
from . import auth, events, settings

def create_app():
    app = Flask(__name__)

    auth.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(events.bp)
    app.register_blueprint(settings.bp)

    return app

# for just running this file
if __name__ == '__main__':
    server = create_app()
    server.run()