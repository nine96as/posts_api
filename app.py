from application import app
from application import routes
from application.posts import routes

if __name__ == "__main__":
    app.run(port=3000, debug=True)