from mongoengine import Document, ReferenceField, StringField

from .user import User


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, required=True)

    meta = {'collection': 'posts'}

    def __repr__(self):
        return f'<Post {self.title} by {self.author.username}>'
