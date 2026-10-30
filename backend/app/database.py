from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.security.config import settings

def get_database():
    engine = create_engine(settings.database_url)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield session