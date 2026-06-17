from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Agregamos connect_args para desactivar los prepared statements en psycopg3
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"prepare_threshold": None}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()