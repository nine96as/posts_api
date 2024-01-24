from flask import jsonify, request
from werkzeug import exceptions
from .models import Post
from .. import db

def index():
    try:
        posts = Post.query.all()
        return jsonify({ 
            "count": len(posts), 
            "data": [p.json for p in posts] 
        }), 200
    except:
        raise exceptions.InternalServerError(f'The server unfortunately ran into an error when attempting to fetch all posts.')


def show(id):
    try:
        post = Post.query.filter_by(id=id).first()
        return jsonify({
            "data": post.json
        }), 200
    except:
        raise exceptions.NotFound(f'The inputted post was not found.')


def create():
    # try:
        title, content, user_id = request.json.values()
        post = Post(title=title, content=content, user_id=user_id)

        db.session.add(post)
        db.session.flush()
        db.session.commit()
        
        return jsonify({
            "data": post.json
        }), 201
    # except:
    #     raise exceptions.BadRequest(f'We could not process your request.')


def update(id):
    try:
        data = request.json
        post = Post.query.filter_by(id=id).first()

        for (attribute, value) in data.items():
            if hasattr(post, attribute):
                setattr(post, attribute, value)

        db.session.commit()

        return jsonify({
            "data": post.json
        }), 200
    except:
        raise exceptions.NotFound(f'The inputted post was not found.')


def destroy(id):
    # try:
        post = Post.query.filter_by(id=id).first()

        db.session.delete(post)
        db.session.commit()

        return "Post Deleted", 204
    # except:
    #     raise exceptions.NotFound(f'The inputted post was not found.')