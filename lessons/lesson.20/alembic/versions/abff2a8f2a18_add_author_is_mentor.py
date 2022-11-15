"""add author.is_mentor

Revision ID: abff2a8f2a18
Revises: ee136cb8c094
Create Date: 2022-10-28 23:19:56.408172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "abff2a8f2a18"
down_revision = "ee136cb8c094"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "authors",
        sa.Column("is_mentor", sa.Boolean(), server_default="FALSE", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("authors", "is_mentor")
    # ### end Alembic commands ###
