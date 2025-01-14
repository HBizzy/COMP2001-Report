from flask import Flask, render_template
from flasgger import Swagger
from routes.trail_routes import setup_routes

app = Flask(__name__)
swagger = Swagger(app)

setup_routes(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




