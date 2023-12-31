from mongoengine import BooleanField, Document, EmailField, StringField


class User(Document):
    username = StringField(max_length=255, unique=True)
    email = EmailField(max_length=255, unique=True, null=True)
    password = StringField(max_length=255, null=False)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)

    meta = {'collection': 'users'}

    def __repr__(self):
        return f"<User {self.username}>"
