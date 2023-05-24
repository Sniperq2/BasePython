"""create table posts

Revision ID: a50ce876287c
Revises: 9d5008253355
Create Date: 2023-05-10 20:40:22.555060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a50ce876287c"
down_revision = "9d5008253355"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "blog_posts",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("title", sa.String(length=90), nullable=False),
        sa.Column("body", sa.Text(), server_default="", nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["blog_authors.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("blog_posts")
    # ### end Alembic commands ###
