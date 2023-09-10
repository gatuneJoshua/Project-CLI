import click
from lib.database import SessionLocal
from lib.models.book import Book
from lib.models.checkout import Checkout

# Create a decorator function to handle database sessions
def with_session(func):
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    return wrapper

@click.command()
@click.argument('book_id', type=int)
@click.argument('borrower_id', type=int)
@with_session
def checkout_book(session, book_id, borrower_id):
    # Retrieve the book from the database
    book = session.query(Book).filter(Book.id == book_id).first()

    if not book:
        click.echo(f"Book with ID {book_id} not found.")
        return

    # Check if the book is already checked out
    if book.is_checked_out:
        click.echo(f"Book '{book.title}' is already checked out.")
        return

    # Create a Checkout record
    checkout = Checkout(book_id=book_id, borrower_id=borrower_id,)

    # Update book status
    book.is_checked_out = True

    # Add the Checkout record to the database
    session.add(checkout)
    click.echo(f"Book '{book.title}' checked out successfully.")

if __name__ == '__main__':
    checkout_book()
