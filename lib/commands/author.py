import click
from lib.database import SessionLocal
from lib.models.author import Author

@click.group()
def author():
    """Manage authors."""
    pass

@author.command()
@click.argument('name')

def add(name,):
    """Add a new author."""
    session = SessionLocal()
    author = Author(name=name,)
    session.add(author)
    session.commit()
    session.close()
    click.echo(f'Author "{name}" added successfully!')

@author.command()
def list():
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

@author.command()
@click.argument('author_id', type=int)
def view(author_id):
    """View author details."""
    session = SessionLocal()
    author = session.query(Author).filter(Author.id == author_id).first()
    session.close()

    if not author:
        click.echo(f'Author with ID {author_id} not found.')
    else:
        click.echo(f'Author ID: {author.id}')
        click.echo(f'Name: {author.name}')
       

if __name__ == '__main__':
    author()
