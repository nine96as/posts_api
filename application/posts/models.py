from application import db, app
from sqlalchemy.sql import func

app.app_context().push()

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    title = db.mapped_column(db.String(100), nullable=False)
    content = db.mapped_column(db.String(500), nullable=False)
    created_at = db.mapped_column(db.DateTime, default=func.now())
    last_modified = db.mapped_column(db.DateTime, onupdate=func.now())
    user_id = db.mapped_column(db.ForeignKey('users.id'))

    user_relationship = db.relationship('User', back_populates='posts_relationship')

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
