from fastapi import FastAPI
import sqlite3


class Product:
    def __init__(self, name, count, brand, size, price):
        self.name = name
        self.count = count
        self.brand = brand
        self.size = size
        self.price = price

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()
cursor.execute('''create table shoes (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                        name text, count integer, 
                                        brand text, 
                                        size integer, 
                                        price integer)''')

app = FastAPI()

@app.on_event("startup")
async def startup():
    with open("file.txt", "r") as f:
        rows = f.readlines()
        for row in rows:
            fields = row.split(' ')
            cursor.execute(f'INSERT INTO shoes (id, name, count, brand, size, price)'
                           f"values('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}','{fields[5]}')")
    connection.commit()

@app.get("/add")
async def addProduct(name, count, brand, size, price):
    print(Product(name, count, brand, size, price))

