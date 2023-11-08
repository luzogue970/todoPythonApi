from app.model.todo import Todo
from app import db  # Assuming "db" is your SQLAlchemy instance
from flask import Blueprint, jsonify, request

todo_bp = Blueprint('posts', __name__)


@todo_bp.route('/get_all', methods=['GET'])
def get_posts():
    posts = Todo.query.all()
    response = jsonify([post.serialize() for post in posts])
    return response, 200


@todo_bp.route('/get/<int:id>', methods=['GET'])
def get_post(id):
    post = Todo.query.get(id)
    if post is not None:
        response = jsonify(post.serialize())
        return response, 200
    else:
        return jsonify({"message": "Post not found"}), 404


@todo_bp.route('/post', methods=['POST'])
def post_posts():
    data = request.json  # Assuming you're sending JSON data in the request
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    new_todo = Todo(content=data['content'], completed=data['completed'])

    # posts = Post.query.add_entity(new_todo)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"message": "Post created successfully"}), 201
