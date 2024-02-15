import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Read db configuration from JSON
credentials_directory = os.path.dirname(__file__)
credentials_path = os.path.join(credentials_directory, 'Credentials/pg_config.json')

with open(credentials_path, 'r') as json_file:
    data = json.load(json_file)
    user = data["user"]
    password = data["password"]
    database = data["database"]
    server = data["server"]
    charset = "utf-8"

db_url = f"postgresql://{user}:{password}@{server}/{database}"

# Function to Create Engine
def creating_engine():
    engine = create_engine(db_url)
    return engine

# Function to create the sessions
def creating_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# Function to close the session
def closing_session(session):
    session.close()

# Function to Dispose Engine
def disposing_engine(engine):
    engine.dispose()
    print("engine closed")