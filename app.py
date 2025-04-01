from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Any app configurations or routes
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    return app
