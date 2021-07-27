from flask_sqlalchemy import SQLAlchemy
from random import randint #Libreria para crear numeros aleatorios

db = SQLAlchemy()

class FamilyTree:
    def __init__(self, lastName):
        self.lastName = lastName

        self.members = [{
            'id': self.generateId(),
            'fistName': 'Luis',
            'lastName': self.lastName,
            'age': 28,
            'luckyNumber': [11,10]
        },{
            'id': self.generateId(),
            'fistName': 'Joana',
            'lastName': self.lastName,
            'age': 29,
            'luckyNumber': [13]
        },{
            'id': self.generateId(),
            'fistName': 'Mikkel',
            'lastName': self.lastName,
            'age': 29,
            'luckyNumber': [13]
        },{
            'id': self.generateId(),
            'fistName': 'Leon',
            'lastName': self.lastName,
            'age': 29,
            'luckyNumber': [13]
        }
        ]

    def generateId(self):   
        return randint(0,99999999) #Genero el id aleatorio
    
    def addMember(self,{data}):





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }