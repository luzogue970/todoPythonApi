from flask import Flask
from flask_cors import CORS
from app.routes.routes import todo_bp
from app import db
from waitress import serve

app = Flask(__name__)
app.register_blueprint(todo_bp)

# Allow all origins for demonstration purposes.
# You should restrict this to specific origins in production.
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:todo@db/todo_items'

if __name__ == 'main':
    with app.app_context():
        db.create_all()
    app.json.sort_keys = False
    app.run()

with app.app_context():
    db.init_app(app)

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5001)
    serve(app, host="0.0.0.0", port=5001)

