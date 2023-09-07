import click
from lib.database import SessionLocal
from lib.models.book import Book
from lib.models.checkout import Checkout

@click.command()
@click.argument('book_id', type=int)
@click.argument('borrower_id', type=int)
def checkout_book(book_id, borrower_id):
    session = SessionLocal()
    
    # Retrieve the book from the database
    book = session.query(Book).filter(Book.id == book_id).first()
    
    if not book:
        click.echo(f"Book with ID {book_id} not found.")
        session.close()
        return
    
    # Check if the book is already checked out
    if book.is_checked_out:
        click.echo(f"Book '{book.title}' is already checked out.")
        session.close()
        return
       
    # Create a Checkout record
    checkout = Checkout(book_id=book_id, borrower_id=borrower_id,)
    
    # Update book status
    book.is_checked_out = True
    
    # Add the Checkout record to the database
    session.add(checkout)
    session.commit()
    
    click.echo(f"Book '{book.title}' checked out successfully.")
    session.close()

