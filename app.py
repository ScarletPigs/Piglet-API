"""Piglet API

Used to run the Piglet API and handle requests about the schedule.
Will be split into multiple files in the future.

Todo:
    * Add DLC poll functionality
    * Keep track of modlists
"""
from flask import Flask
from src.services.database import Database
from src.routes.routes import Blueprint

# Define constants and establish flask app
DATABASE_PATH = 'db/db.sqlite3'


# Main function
def main():
    print("Starting Piglet API...")
    
    print("Connecting to database...")
    db = Database(DATABASE_PATH)
    db.connect()
    
    print("Starting Flask app... (Ctrl+C to stop)")
    app = Flask(__name__)
    
    
    
    app.run(debug=True,)


# If ran as main, start the app
if __name__ == '__main__':
    main()