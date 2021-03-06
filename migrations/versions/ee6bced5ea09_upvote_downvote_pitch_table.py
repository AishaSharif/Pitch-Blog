"""Upvote|Downvote pitch table

Revision ID: ee6bced5ea09
Revises: b2f843d4efff
Create Date: 2019-05-29 11:42:43.594430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee6bced5ea09'
down_revision = 'b2f843d4efff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitch', sa.Column('downvote', sa.Integer(), nullable=True))
    op.add_column('pitch', sa.Column('upvote', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('comment_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'comment_id')
    op.drop_column('pitch', 'upvote')
    op.drop_column('pitch', 'downvote')
    op.drop_table('comments')
    # ### end Alembic commands ###
