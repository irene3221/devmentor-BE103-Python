"""create colunm

Revision ID: 688d19a8b48f
Revises: b26a6ace9a35
Create Date: 2024-04-01 00:54:06.184104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '688d19a8b48f'
down_revision: Union[str, None] = 'b26a6ace9a35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('events_langs', sa.Column('content', sa.String(length=255), nullable=False))
    op.drop_column('events', 'content')

def downgrade() -> None:
    op.drop_column('events', 'version')
    op.drop_column('events', 'previous_version')

