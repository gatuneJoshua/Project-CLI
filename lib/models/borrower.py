from sqlalchemy import Column, Integer, String
from lib.models.checkout import Checkout  # Import the Checkout model
from lib.database import Base

class Borrower(Base):
    __tablename__ = 'borrowers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def borrow_book(self, book, session):
        try:
            # Check if the book is available for borrowing
            if book.is_available_for_borrowing(session):
                # Create a new Checkout record
                checkout = Checkout(book_id=book.id, borrower_id=self.id)
                
                # Update the book's status (for example, mark it as borrowed)
                book.borrowed = True

                # Add the checkout record to the session and commit the transaction
                session.add(checkout)
                session.commit()
                
                print(f"{self.name} has successfully borrowed '{book.title}'.")
            else:
                print(f"'{book.title}' is not available for borrowing.")
        except Exception as e:
            session.rollback()
            print(f"An error occurred while borrowing '{book.title}': {str(e)}")
