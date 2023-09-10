import click
from lib.database import SessionLocal
from lib.models.book import Book

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

@click.group()
def book():
    """Manage books."""
    pass

@book.command()
@click.argument('title')
@click.argument('author_id', type=int)
@with_session
def add(session, title, author_id):
    """Add new book."""
    book = Book(title=title, author_id=author_id)
    session.add(book)
    click.echo(f'Book "{title}" added successfully!')

@book.command()
@with_session
def list(session):
    """List all books."""
    books = session.query(Book).all()

    if not books:
        click.echo('No books found.')
    else:
        click.echo('Books:')
        for book in books:
            click.echo(f'- ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}')

@book.command()
@click.argument('book_id', type=int)
@with_session
def view(session, book_id):
    """View book details."""
    book = session.query(Book).filter(Book.id == book_id).first()

    if not book:
        click.echo(f'Book with ID {book_id} not found.')
    else:
        click.echo(f'Book ID: {book.id}')
        click.echo(f'Title: {book.title}')
        click.echo(f'Author ID: {book.author_id}')

if __name__ == '__main__':
    book()
