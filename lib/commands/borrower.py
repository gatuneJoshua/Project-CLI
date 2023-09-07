import click
from lib.database import SessionLocal
from lib.models.borrower import Borrower

@click.group()
def borrower():
    """Manage borrowers."""
    pass

@borrower.command()
@click.argument('name')

def add(name):
    """Add a new borrower."""
    session = SessionLocal()
    borrower = Borrower(name=name,)
    session.add(borrower)
    session.commit()
    session.close()
    click.echo(f'Borrower "{name}" added successfully!')

@borrower.command()
def list():
    """List all borrowers."""
    session = SessionLocal()
    borrowers = session.query(Borrower).all()
    session.close()

    if not borrowers:
        click.echo('No borrowers found.')
    else:
        click.echo('Borrowers:')
        for borrower in borrowers:
            click.echo(f'- ID: {borrower.id}, Name: {borrower.name},')

@borrower.command()
@click.argument('borrower_id', type=int)
def view(borrower_id):
    """View borrower details."""
    session = SessionLocal()
    borrower = session.query(Borrower).filter(Borrower.id == borrower_id).first()
    session.close()

    if not borrower:
        click.echo(f'Borrower with ID {borrower_id} not found.')
    else:
        click.echo(f'Borrower ID: {borrower.id}')
        click.echo(f'Name: {borrower.name}')
        

if __name__ == '__main__':
    borrower()
