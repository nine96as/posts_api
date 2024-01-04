from application import db, app
from sqlalchemy.sql import func

app.app_context().push()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    posts = db.relationship('Post', backref='users', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'User(id: {self.id}, username: {self.username})'
    
    @property
    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at
        }