from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from lib.models.base import Base

class Borrower(Base):
    __tablename__ = 'borrowers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self, name,):
        self.name = name
    
    def __str__(self):
        return self.name

    def borrow_book(self, book, session):
        # Check if the book is available for borrowing
        if book.is_available_for_borrowing(session):
            # Create a new Checkout record
            checkout = checkout(book=book, borrower=self)
            
            # Update the book's status (for example, mark it as borrowed)
            book.borrowed = True

            # Add the checkout record to the session and commit the transaction
            session.add(checkout)
            session.commit()
            
            print(f"{self.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available for borrowing.")
