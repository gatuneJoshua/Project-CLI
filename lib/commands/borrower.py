import click
from lib.database import SessionLocal
from lib.models.borrower import Borrower

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
def borrower():
    """Manage borrowers."""
    pass

@borrower.command()
@click.argument('name')
@with_session
def add(session, name):
    """Add a new borrower."""
    borrower = Borrower(name=name)
    session.add(borrower)
    click.echo(f'Borrower "{name}" added successfully!')

@borrower.command()
@with_session
def list(session):
    """List all borrowers."""
    borrowers = session.query(Borrower).all()

    if not borrowers:
        click.echo('No borrowers found.')
    else:
        click.echo('Borrowers:')
        for borrower in borrowers:
            click.echo(f'- ID: {borrower.id}, Name: {borrower.name}')

@borrower.command()
@click.argument('borrower_id', type=int)
@with_session
def view(session, borrower_id):
    """View borrower details."""
    borrower = session.query(Borrower).filter(Borrower.id == borrower_id).first()

    if not borrower:
        click.echo(f'Borrower with ID {borrower_id} not found.')
    else:
        click.echo(f'Borrower ID: {borrower.id}')
        click.echo(f'Name: {borrower.name}')

if __name__ == '__main__':
    borrower()
