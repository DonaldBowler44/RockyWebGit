from models.characters import db

class userSchema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__ (self, email, password):
        self.email = email
        self.password = password