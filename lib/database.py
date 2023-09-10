from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define your database URL
DATABASE_URL = "sqlite:///library.db"

# Create an SQLAlchemy engine for the database connection.
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory for creating database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models.
Base = declarative_base()
Base.metadata.create_all(bind=engine)
print("Database initialized")