from utils.db import db
from utils.maconfig import ma


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    celular = db.Column(db.Integer(), nullable=False)
    motivo = db.Column(db.String(50), nullable=False)
    mensaje = db.Column(db.String(500), nullable=False)

    def __init__(self, nombre, apellido, email, celular, motivo, mensaje):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        self.motivo = motivo
        self.mensaje = mensaje

    def __repr__(self):
        return f"<Contact {self.id}: nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}', celular={self.celular}, motivo='{self.motivo}', mensaje='{self.mensaje}'>"


class ContactSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'email', 'celular', 'motivo', 'mensaje')
