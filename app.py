"""Piglet API

Used to run the Piglet API and handle requests about the schedule.
Will be split into multiple files in the future.

Todo:
    * Add DLC poll functionality
    * Keep track of modlists
"""

from src.services.database import *

# Define constants and establish flask app
DATABASE_PATH = 'db/db.sqlite3'


# Main function
def main():
    print("Starting Piglet API...")
    
    print("Connecting to database...")
    db = Database(DATABASE_PATH)
    
    columns = {
        'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'name': 'TEXT NOT NULL',
        'description': 'TEXT NOT NULL',
        'start_time': 'TEXT NOT NULL',
        'end_time': 'TEXT NOT NULL',
        'modlist': 'TEXT NOT NULL',
        'dlc': 'TEXT NOT NULL'
    }
    
    table = db.get_table('schedule', columns)
    
    table.insert_data((None, 'test', 'test', 'test', 'test', 'test', 'test'))
    
    print("Starting Flask app... (Ctrl+C to stop)")
    #app = Flask(__name__)
    #app.run(debug=True,)


# If ran as main, start the app
if __name__ == '__main__':
    main()