from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=True)
    
    # Define a relationship with the Author model
    author = relationship('Author', back_populates='books')
   

    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id
        

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    

   
