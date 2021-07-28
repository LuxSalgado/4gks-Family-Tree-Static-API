from flask_sqlalchemy import SQLAlchemy
from random import randint #Libreria para crear numeros aleatorios
import os

db = SQLAlchemy()

class FamilyTree:
    def __init__(self, lastName):
        self.lastName = lastName

        self.members = [{
            'id': 1,
            'fistName': 'Luis',
            'lastName': self.lastName,
            'age': 28,
            'parent': 3,
            'child': 2,
            'url': os.environ.get('BACKEND_URL')
        },
        {
            'id': 2,
            'fistName': 'Jesus',
            'lastName': self.lastName,
            'age': 5,
            'parent': 1,
            'child': None
        },
        {
            'id': 3,
            'fistName': 'Daniel',
            'lastName': self.lastName,
            'age': 65,
            'parent': None,
            'child': [1,4]
        },
        {
            'id': 4,
            'fistName': 'Patricia',
            'lastName': self.lastName,
            'age': 36,
            'parent': 3,
            'child': 5
        },
        {
            'id': 5,
            'fistName': 'Clara',
            'lastName': self.lastName,
            'age': 2,
            'parent': 4,
            'child': None
        },
        {
            'id': 6,
            'fistName': 'Roberto',
            'lastName': self.lastName,
            'age': 21,
            'parent': 4,
            'child': 7
        },
        {
            'id': 7,
            'fistName': 'Miguel',
            'lastName': self.lastName,
            'age': 3,
            'parent': 6,
            'child': None
        }
        ]

    def generateId(self):   
        return randint(0,99999999) #Genero el id aleatorio
    
    def idMember(self,id): #recorro tod el arreglo y retorno solo lo que coincida con el id
        for i in self.members: #recorrer el arreglo members
                if i['id'] == int(id):
                    return i
        return None


