"""initial

Revision ID: ddaa81309128
Revises: 
Create Date: 2023-09-11 00:23:24.480409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddaa81309128'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('birthdate', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'books',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('author_id', sa.Integer(), sa.ForeignKey('authors.id'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'borrowers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'checkouts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('book_id', sa.Integer(), sa.ForeignKey('books.id'), nullable=False),
        sa.Column('borrower_id', sa.Integer(), sa.ForeignKey('borrowers.id'), nullable=False),
        sa.Column('checkout_date', sa.DateTime(), nullable=False),
        sa.Column('return_date', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('checkouts')
    op.drop_table('borrowers')
    op.drop_table('books')
    op.drop_table('authors')