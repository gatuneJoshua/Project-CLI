import click
from lib.commands import author, book, borrower, checkout

@click.group()
def library():
    """Library M.S."""
    pass

library.add_command(author.author)
library.add_command(book.book)
library.add_command(borrower.borrower)
library.add_command(checkout.checkout)

if __name__ == '__main__':
    library()
