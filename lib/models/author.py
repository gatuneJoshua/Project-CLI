from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from lib.database import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    birthdate = Column(String)

    # Define a relationship with the Book model
    books = relationship('Book', back_populates='author', cascade="all, delete-orphan")

    def __init__(self, name, birthdate=None):
        if len(name) > 255:
            raise ValueError("Author name is too long.")
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return f"Author ID: {self.id}, Name: {self.name}, Birthdate: {self.birthdate}"
