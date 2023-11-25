from flask import Blueprint, request
from src.controllers import event_controller

app = Blueprint('routes', __name__)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event_controller.create_event(data)
    

@app.route('/events/<event_id>', methods=['PUT'])
def edit_event(event_id):
    # Logic for editing an event
    pass

@app.route('/events/<event_id>', methods=['DELETE'])
def remove_event(event_id):
    # Logic for removing an event
    pass

@app.route('/events/<event_id>', methods=['GET'])
def fetch_event(event_id):
    event_controller.fetch_event(event_id)
    pass
