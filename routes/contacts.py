from flask import Blueprint, request, jsonify, abort
from models.contact import Contact, ContactSchema
from utils.db import db

contacts = Blueprint('contacts', __name__)

contact_schema = ContactSchema()
contact_schemas = ContactSchema(many=True)

@contacts.route('', methods=['POST'])
def post_contact():
    try:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        email = request.json['email']
        celular = request.json['celular']
        motivo = request.json['motivo']
        mensaje = request.json['mensaje']

        contact = Contact(
            nombre=nombre,
            apellido=apellido,
            email=email,
            celular=celular,
            motivo=motivo,
            mensaje=mensaje
        )
        db.session.add(contact)
        db.session.commit()

        return contact_schema.jsonify(contact)
    except Exception as e:
        print(e)
        abort(400)

@contacts.route('/<id>', methods=['PUT'])
def update_contact(id):
    try:
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({"message": "Contact not found"}), 404

        contact.nombre = request.json.get('nombre', contact.nombre)
        contact.apellido = request.json.get('apellido', contact.apellido)
        contact.email = request.json.get('email', contact.email)
        contact.celular = request.json.get('celular', contact.celular)
        contact.motivo = request.json.get('motivo', contact.motivo)
        contact.mensaje = request.json.get('mensaje', contact.mensaje)

        db.session.commit()

        return contact_schema.jsonify(contact)
    except Exception as e:
        print(e)
        abort(400)

@contacts.route('', methods=['GET'])
def get_contacts():
    try:
        contacts = Contact.query.all()
        serialized_contacts = contact_schemas.dump(contacts)
        return jsonify(serialized_contacts)
    except Exception as e:
        print(e)
        abort(400)

@contacts.route('/<id>', methods=['GET'])
def get_contact(id):
    try:
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({"message": "Contact not found"}), 404

        serialized_contact = contact_schema.dump(contact)
        return jsonify(serialized_contact)
    except Exception as e:
        print(e)
        abort(400)

@contacts.route('/<id>', methods=['DELETE'])
def delete_contact(id):
    try:
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({"message": "Contact not found"}), 404

        db.session.delete(contact)
        db.session.commit()

        return jsonify({"message": "Contact deleted successfully"}), 200
    except Exception as e:
        print(e)
        abort(400)
