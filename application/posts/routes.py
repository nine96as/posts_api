from flask import jsonify, request
from application import app
from werkzeug import exceptions
from .controllers import index, create, show, update, destroy

@app.route('/posts', methods=["GET", "POST"])
def handle_posts():
    if request.method == 'POST': return create()
    else: return index()


@app.route('/posts/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_post(id):
    if request.method == "GET": return show(id)
    elif request.method == "PATCH": return update(id)
    elif request.method == "DELETE": return destroy(id)


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error": f"Oops {err}"}), 400

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Oops {err}"}), 500