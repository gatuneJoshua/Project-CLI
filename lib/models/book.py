from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.models.checkout import Checkout  

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    # Define a relationship with the Author model
    author = relationship('Author', back_populates='books')

    def __init__(self, title, author):
        self.title = title
        self.author = author
        

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    

    # Check if the book is currently checked out by any borrower    
    def is_available_for_borrowing(self, session):
        checkout = session.query(Checkout).filter(
            Checkout.book_id == self.id,
            Checkout.returned_date.is_(None)  # Check if the book is not returned
        ).first()

        return not checkout  # True if the book is not checked out
