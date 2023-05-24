from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'INDEX'

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        messages = []

        for message in Message.query.all():
            messages.append(message.to_dict())

        response = make_response(messages, 200)
        return response
    
    elif request.method == 'POST':
        data = request.get_json()

        new_message = Message(
            body=data['body'],
            username=data['username']
        )

        db.session.add(new_message)
        db.session.commit()

        response = make_response(new_message.to_dict(), 201)
        return response

@app.route('/messages/<int:id>', methods = ['PATCH', 'DELETE'])
def messages_by_id(id):

    message = Message.query.filter(Message.id == id).first()

    if request.method == 'PATCH':
        for attr in message.getattr():
            setattr(message, attr, )

    elif request.method == 'DELETE':
        db.sesion.delete(message)
        db.session.commit()

        response_body = {
            "successfully-deleted": True,
            "Message": "Message successfully deleted"
        }
        response = make_response(response_body, 200)
        return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
