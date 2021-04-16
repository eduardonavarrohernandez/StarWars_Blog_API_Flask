from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    mail = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "mail": self.mail,
            # do not serialize the password, its a security breach
        }
class Personajes(db.Model):
    __tablename__ = 'personajes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)

class Planetas(db.Model):
    __tablename__ = 'planetas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)


class Favoritos(db.Model):
    __tablename__ = 'favoritos'

    id = db.Column(db.Integer, primary_key=True)

    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    User = db.relationship(User)
    tipoFavorito = db.Column(db.String(250), nullable=False)
    favoritoId = db.Column(db.String(250), nullable=False)

