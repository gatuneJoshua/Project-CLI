import click

# Dummy data for demonstration purposes
books_database = []
authors_database = []

@click.group()
def library():
    """Library Management CLI"""
    pass

@library.command()
@click.argument("title")
@click.argument("author")
def book(title, author):
    """Manage books"""
    add_book(title, author)
    print("Book added successfully.")

@library.command()
@click.argument("name")
def author(name):
    """Manage authors"""
    add_author(name)
    print("Author added successfully.")

@library.command()
@click.argument("entity", type=click.Choice(["books", "authors"]))
def list(entity):
    """List books or authors"""
    if entity == "books":
        list_books()
    elif entity == "authors":
        list_authors()

def add_book(title, author):
    books_database.append({"title": title, "author": author})

def add_author(name):
    authors_database.append({"name": name})

def list_books():
    for book in books_database:
        print(f"Title: {book['title']}, Author: {book['author']}")

def list_authors():
    for author in authors_database:
        print(f"Author: {author['name']}")

if __name__ == "_main_":
    library()