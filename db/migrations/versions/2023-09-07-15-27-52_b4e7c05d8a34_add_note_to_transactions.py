"""Add note to transactions

Revision ID: b4e7c05d8a34
Revises: 30643169b049
Create Date: 2023-09-07 15:27:52.951907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4e7c05d8a34'
down_revision: Union[str, None] = '30643169b049'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('note', sa.String(), nullable=True))
    op.create_index(op.f('ix_transactions_note'), 'transactions', ['note'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transactions_note'), table_name='transactions')
    op.drop_column('transactions', 'note')
    # ### end Alembic commands ###
