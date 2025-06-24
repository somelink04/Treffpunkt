from flask import Flask
from . import auth

def create_app():
    app = Flask(__name__,
                static_url_path='/',
                static_folder='../front/build')

    @app.route(rule='/', defaults={'p': ''})
    @app.route(rule="/<path:p>", methods=["GET"])
    def serve_front(p):
        return app.send_static_file('index.html')

    auth.init_app(app)
    app.register_blueprint(auth.bp)

    return app

# for just running this file
if __name__ == '__main__':
    server = create_app()
    server.run()