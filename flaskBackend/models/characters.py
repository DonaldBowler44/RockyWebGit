from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    height = db.Column(db.String(20))
    weight = db.Column(db.String(20))
    total_fights = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    wins_by_ko = db.Column(db.Integer)
    draws = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    stance = db.Column(db.String(50))

    def __init__ (self, name, height, weight, total_fights, wins, wins_by_ko, draws, losses, stance):
        self.name = name
        self.height = height
        self.weight = weight
        self.total_fights = total_fights
        self.wins = wins
        self.wins_by_ko = wins_by_ko
        self.draws = draws
        self.losses = losses
        self.stance = stance