from services.database import Database

def create_event(data : dict):
    db = Database()
    db.connect()
    db.add_entry("events", data)
    db.disconnect()

def fetch_event(event_id):
    db = Database()
    db.connect()
    event = db.fetch_entry("events", f"id={event_id}")
    db.disconnect()
    return event