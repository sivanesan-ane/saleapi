"""Change sale id from UUID to BigInteger

Revision ID: e48b2a19f5d3
Revises: c98aed54d952
Create Date: 2026-11-23 10:04:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e48b2a19f5d3'
down_revision = 'c98aed54d952'
branch_labels = None
depends_on = None


def upgrade():
    # Drop primary key constraint and replace id with autoincrementing BigInteger
    # Since existing table has data with UUIDs, we drop the UUID id column and add a bigserial id
    op.execute("ALTER TABLE sales DROP CONSTRAINT IF EXISTS sales_pkey CASCADE")
    op.execute("ALTER TABLE sales DROP COLUMN id")
    op.execute("ALTER TABLE sales ADD COLUMN id BIGSERIAL PRIMARY KEY")


def downgrade():
    op.execute("ALTER TABLE sales DROP CONSTRAINT IF EXISTS sales_pkey CASCADE")
    op.execute("ALTER TABLE sales DROP COLUMN id")
    op.execute("ALTER TABLE sales ADD COLUMN id UUID PRIMARY KEY DEFAULT gen_random_uuid()")
