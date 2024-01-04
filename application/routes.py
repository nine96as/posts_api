from flask import jsonify
from application import app

@app.route('/')
def hello():
    return jsonify({
        "name": "Posts API",
        "description": "Interact with the Posts API through the routes below.",
        "endpoints": [
            "GET /",
            "GET /posts",
            "GET /posts/:id",
            "POST /posts/:id",
            "PATCH /posts/:id",
            "DELETE /posts/:id"
        ]
    }), 200