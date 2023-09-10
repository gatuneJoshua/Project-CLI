import click
from lib.database import SessionLocal
from lib.models.author import Author

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
def author():
    """Manage authors."""
    pass

@author.command()
@click.argument('name')
@with_session
def add(session, name):
    """Add a new author."""
    author = Author(name=name)
    session.add(author)
    click.echo(f'Author "{name}" added successfully!')

@author.command()
@with_session
def list(session):
    """List all authors."""
    authors = session.query(Author).all()

    if not authors:
        click.echo('No authors found.')
    else:
        click.echo('Authors:')
        for author in authors:
            click.echo(f'- ID: {author.id}, Name: {author.name}')

@author.command()
@click.argument('author_id', type=int)
@with_session
def view(session, author_id):
    """View author details."""
    author = session.query(Author).filter(Author.id == author_id).first()

    if not author:
        click.echo(f'Author with ID {author_id} not found.')
    else:
        click.echo(f'Author ID: {author.id}')
        click.echo(f'Name: {author.name}')

if __name__ == '__main__':
    author()
