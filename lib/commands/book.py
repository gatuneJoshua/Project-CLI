import click
from lib.database import SessionLocal
from lib.models.book import Book

@click.group()
def book():
    """Manage books."""
    pass

@book.command()
@click.argument('title')
@click.argument('author_id', type=int)
def add(title, author_id):
    """Add new book."""
    session = SessionLocal()
    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    session.close()
    click.echo(f'Book "{title}" added successfully!')

@book.command()
def list():
    """List all books."""
    session = SessionLocal()
    books = session.query(Book).all()
    session.close()

    if not books:
        click.echo('No books found.')
    else:
        click.echo('Books:')
        for book in books:
            click.echo(f'- ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}')

@book.command()
@click.argument('book_id', type=int)
def view(book_id):
    """View book details."""
    session = SessionLocal()
    book = session.query(Book).filter(Book.id == book_id).first()
    session.close()

    if not book:
        click.echo(f'Book with ID {book_id} not found.')
    else:
        click.echo(f'Book ID: {book.id}')
        click.echo(f'Title: {book.title}')
        click.echo(f'Author ID: {book.author_id}')

if __name__ == '__main__':
    book()
