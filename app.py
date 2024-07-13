from flask import Flask, render_template, request, redirect, url_for
import datetime

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():
        return "Hello world test"

    if __name__ == '__main__':
        app.run(debug=False , host='0.0.0.0' )

    return app