import click
from lib.database import SessionLocal, Base, engine
from lib.models.author import Author
from lib.models.book import Book

# Create a CLI group for the main application
@click.group()
def library_cli():
    pass

# Command to add a new author
@library_cli.command()
@click.argument('name')
def add_author(name):
    """Add a new author."""
    session = SessionLocal()
    author = Author(name=name)
    session.add(author)
    session.commit()
    session.close()
    click.echo(f'Author "{name}" added successfully!')

# Command to update an author's name
@library_cli.command()
@click.argument('author_id', type=int)
@click.argument('new_name')
def update_author(author_id, new_name):
    """Update an author's name."""
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()

    if not author:
        session.close()
        click.echo(f'Author with ID {author_id} not found.')
        return

    author.name = new_name
    session.commit()
    session.close()
    click.echo(f'Author with ID {author_id} updated to "{new_name}" successfully!')

# Command to delete an author
@library_cli.command()
@click.argument('author_id', type=int)
def delete_author(author_id):
    """Delete an author."""
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()

    if not author:
        session.close()
        click.echo(f'Author with ID {author_id} not found.')
        return

    session.delete(author)
    session.commit()
    session.close()
    click.echo(f'Author with ID {author_id} deleted successfully!')


# Command to list all authors
@library_cli.command()
def list_authors():
    """List all authors."""
    session = SessionLocal()
    authors = session.query(Author).all()
    session.close()

    if not authors:
        click.echo('No authors found.')
    else:
        click.echo('Authors:')
        for author in authors:
            click.echo(f'- ID: {author.id}, Name: {author.name},')

# Command to add a new book
@library_cli.command()
@click.argument('title')
@click.argument('author_id', type=int)
def add_book(title, author_id):
    """Add a new book."""
    session = SessionLocal()
    author = session.query(Author).filter_by(id=author_id).first()

    if not author:
        session.close()
        click.echo(f'Author with ID {author_id} not found.')
        return

    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    session.close()
    click.echo(f'Book "{title}" by {author.name} added successfully!')

# Command to list all books
@library_cli.command()
def list_books():
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

# Command to update a book's title
@library_cli.command()
@click.argument('book_id', type=int)
@click.argument('new_title')
def update_book(book_id, new_title):
    """Update a book's title."""
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()

    if not book:
        session.close()
        click.echo(f'Book with ID {book_id} not found.')
        return

    book.title = new_title
    session.commit()
    session.close()
    click.echo(f'Book with ID {book_id} updated to "{new_title}" successfully!')

# Command to delete a book
@library_cli.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    """Delete a book."""
    session = SessionLocal()
    book = session.query(Book).filter_by(id=book_id).first()

    if not book:
        session.close()
        click.echo(f'Book with ID {book_id} not found.')
        return

    session.delete(book)
    session.commit()
    session.close()
    click.echo(f'Book with ID {book_id} deleted successfully!')

if __name__ == '__main__':
    library_cli()
