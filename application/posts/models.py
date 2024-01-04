from application import db, app
from sqlalchemy.sql import func

app.app_context().push()

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    last_modified = db.Column(db.DateTime, onupdate=func.now())

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f'Post(id: {self.id}, title: {self.name})'

    @property
    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "last_modified": self.last_modified
        }
