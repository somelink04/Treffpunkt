from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__,
                static_folder="../front",
                static_url_path="/")

    @app.route(rule='/hi', defaults={'name': 'client'})
    @app.route('/hi/<name>')
    def say_hi(name):
        return jsonify({'reply': f'Hello, {name}!'})

    @app.route(rule='/', defaults={'path': ''})
    @app.route(rule='/<path>')
    def get_front(path):
        return app.send_static_file('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()