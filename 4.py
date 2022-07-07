from fastapi import FastAPI
import sqlalchemy
import uvicorn
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///db/shoe.db"
metadata = sqlalchemy.MetaData()
product = sqlalchemy.Table("product", metadata,
                           sqlalchemy.Column("id", sqlalchemy.Integer(), primary_key=True, autoincrement=True),
                           sqlalchemy.Column("name", sqlalchemy.String()),
                           sqlalchemy.Column("count", sqlalchemy.Integer()),
                           sqlalchemy.Column("brand", sqlalchemy.String()),
                           sqlalchemy.Column("size", sqlalchemy.Integer()),
                           sqlalchemy.Column("price", sqlalchemy.Integer()),
                           )
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()


@app.on_event("startup")
async def startup():
    product.create(engine, checkfirst=True)


@app.on_event("shutdown")
async def shutdown():
    conn.close()


@app.get("/add")
async def add_product(name, count, brand, size, price):
    stmt = (
        sqlalchemy.insert(product).
            values(name=name, count=count, brand=brand, size=size, price=price)
    )
    conn.execute(stmt)


@app.get("/delete")
async def delete_product(id):
    stmt = (
        sqlalchemy.delete(product).
            where(product.c.id == id)
    )
    conn.execute(stmt)


@app.get("/add_all_products")
async def add_all_products():
    with open("file3.txt", "r") as f:
        rows = f.readlines()
        for row in rows:
            fields = row.split(' ')
            stmt = (
                sqlalchemy.insert(product).
                    values(name=fields[1], count=fields[2], brand=fields[3], size=fields[4], price=fields[5])
            )
            conn.execute(stmt)


@app.get(
    "/show",
    response_description="Все товары",
)
async def show():
    d = product.select()
    result = conn.execute(d)
    prods = []
    for row in result:
        prods.append(row)
    return prods


@app.get(
    "/show_stat"
)
async def show_statistics():
    d = product.select()
    result = conn.execute(d)
    prods = []
    for row in result:
        prods.append(row)
    brands = dict()
    sizes = dict()
    for name in prods:
        brand = name["brand"]
        size = name["size"]

        if brand in brands:
            brands[brand] += name["count"]
        else:
            brands[brand] = name["count"]

        if size in sizes:
            sizes[size] += name["count"]
        else:
            sizes[size] = name["count"]
    return brands, sizes


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)