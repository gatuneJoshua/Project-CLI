from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.base import Base
from sqlalchemy.orm import Session



class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    # Define a relationship with the Author model
    author = relationship('Author', back_populates='books')

    # initializing book objects and a __str__ method to provide a readable string representation of the book.
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    def is_available_for_borrowing(self, session):
        # Check if the book is currently checked out by any borrower
        checkout = session.query(checkout).filter_by(book=self).first()
        
        if checkout:
            # The book is checked out, check if it's overdue
            return not self.is_overdue(checkout)
        else:
            # The book is not checked out
            return True
    
    