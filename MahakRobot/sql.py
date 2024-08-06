from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (replace with your actual database URL)
DATABASE_URL = 'postgresql://user:password@localhost/your_database'

# Create engine and base
engine = create_engine(DATABASE_URL)
BASE = declarative_base()
Session = sessionmaker(bind=engine)
SESSION = Session()
