import os
import json

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker, Session


DB_CREDENTIALS = json.loads(os.getenv('DB_CREDENTIALS', '{}'))

connection_string = str(URL.create(**DB_CREDENTIALS))
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()