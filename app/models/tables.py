from app import db


class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String)
    nome = db.Column(db.String(120))
    email = db.Column(db.String, unique=True)
    
    def __init__(self, username, password, nome, email):
        self.username = username
        self.password = password
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return "<User %r>" % self.username       

class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.String(120), unique=True)
    nome = db.Column(db.String(120))
    email = db.Column(db.String, unique=True)
    
    def __init__(self, username, password, nome, email):
        self.username = username
        self.password = password
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return "<User %r>" % self.username       