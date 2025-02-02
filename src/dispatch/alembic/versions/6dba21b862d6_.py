"""Adds additional task cascade.

Revision ID: 6dba21b862d6
Revises: e45e8226932a
Create Date: 2021-03-17 11:59:17.270356

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "6dba21b862d6"
down_revision = "e45e8226932a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("task_creator_id_fkey", "task", type_="foreignkey")
    op.drop_constraint("task_owner_id_fkey", "task", type_="foreignkey")
    op.create_foreign_key(None, "task", "participant", ["creator_id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key(None, "task", "participant", ["owner_id"], ["id"], ondelete="CASCADE")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "task", type_="foreignkey")
    op.drop_constraint(None, "task", type_="foreignkey")
    op.create_foreign_key("task_owner_id_fkey", "task", "participant", ["owner_id"], ["id"])
    op.create_foreign_key("task_creator_id_fkey", "task", "participant", ["creator_id"], ["id"])
    # ### end Alembic commands ###
