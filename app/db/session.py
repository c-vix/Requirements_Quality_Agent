from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def init_db():
    from app.db import tables
    with engine.beign() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXIST vector"))
    Base.metadata.create_all(engine)