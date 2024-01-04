from application import db, app
from sqlalchemy.sql import func

app.app_context().push()

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, onupdate=func.now())
    user_id = db.mapped_column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'Post(id: {self.id}, title: {self.title}, user_id: {self.user_id})'

    @property
    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "last_modified": self.last_modified,
            "user_id": self.user_id
        }
