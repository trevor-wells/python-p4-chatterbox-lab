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
        new_message = Message(
            body: request.get_json()
            
        )
@app.route('/messages/<int:id>', methods = ['PATCH', 'DELETE'])
def messages_by_id(id):
    return ''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
