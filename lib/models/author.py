from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models.base import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Define a relationship with the Book model
    books = relationship('Book', back_populates='author')

    # initializing author objects and a __str__ method to provide readable string representation of the author.
    def __init__(self, name,):
        self.name = name
        
    def __str__(self):
        return self.name
