from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DBConfig

db_config = DBConfig()

SQLALCHEMY_DATABASE_URL = f"mysql://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
