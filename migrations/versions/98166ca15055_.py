"""empty message

Revision ID: 98166ca15055
Revises: dbb79ff12e45
Create Date: 2016-05-23 13:05:50.163693
Modified Date: 2016-06-04

"""

# revision identifiers, used by Alembic.
revision = '98166ca15055'
down_revision = 'dbb79ff12e45'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('contact', sa.String(), nullable=True),
    sa.Column('facebook', sa.String(), nullable=True),
    sa.Column('twitter', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'events', sa.Column('closing_datetime', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'events', 'closing_datetime')
    op.drop_table('user_detail')
    ### end Alembic commands ###
