from flask import Flask, render_template


def create_app(test_config=None):

    # App Config
    app = Flask(__name__)

    # ---------------------------------------- #
    # Endpoints
    # ---------------------------------------- #
    @app.route('/')
    def index():
        return render_template('home.html')

    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
