from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from lib.models.base import Base

class Checkout(Base):
    __tablename__ = 'checkouts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    borrower_id = Column(Integer, ForeignKey('borrowers.id'), nullable=False)
    checkout_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)  # Add a field for the return date

    # Define relationships with the Book and Borrower models
    book = relationship('Book', back_populates='checkouts')
    borrower = relationship('Borrower', back_populates='checkouts')

    def __init__(self, book, borrower, checkout_date):
        self.book = book
        self.borrower = borrower
        self.checkout_date = checkout_date

    # Add additional methods as needed
    def mark_as_returned(self, return_date):
        # Mark the checkout record as returned and set the return date
        self.return_date = return_date