import typing
import random
from pydantic import BaseModel
from pydantic import Field
from sqlalchemy import MetaData, Table, String, Integer, Column, Text

metadata = MetaData()

products = Table("products", metadata,
    sqlalchemy.Column("id", Integer(), primary_key=True),
    sqlalchemy.Column("name", String()),
    sqlalchemy.Column("count", Integer()),
    sqlalchemy.Column("brand", String()),
    sqlalchemy.Column("size", Integer()),
    sqlalchemy.Column("price", Integer()),
)

