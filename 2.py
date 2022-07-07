import sqlite3

print('Добро пожаловать!')
print('для добавления нового товара введите 1')
print('для отображения всех товаров введите 2')
print('для ввода товаров из файла введите 3')
print('для удаления товара  введите 4')
print('для вывода статистики введите 5')
print('для выхода введите 0')

products = []

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()
cursor.execute('''create table if not exists shoes (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                        name text, count integer, 
                                        brand text, 
                                        size integer, 
                                        price integer)''')

def readfileonstart():
    s = open("file3.txt", "r")
    lines = s.readlines()

    for line in lines:
        linesplit = line.split(" ")
        product = {"id": int(linesplit[0]),
                   "name": str(linesplit[1]),
                   "count": int(linesplit[2]),
                   "brand": str(linesplit[3]),
                   "size": int(linesplit[4]),
                   "price": int(linesplit[5])}
        products.append(product)

with open("file3.txt", "r") as f:
    rows = f.readlines()
    for row in rows:
        fields = row.split(' ')
        cursor.execute(f'INSERT INTO shoes (name, count, brand, size, price)' 
                       f"values('{fields[1]}','{fields[2]}','{fields[3]}','{fields[4]}','{fields[5]}')")
connection.commit()

readfileonstart()

def readfile():
    r = open("file4.txt", "r")
    lines = r.readlines()

    for line in lines:
        linesplit = line.split(" ")
        prod = {"id": int(linesplit[0]),
                   "name": str(linesplit[1]),
                   "count": int(linesplit[2]),
                   "brand": str(linesplit[3]),
                   "size": int(linesplit[4]),
                   "price": int(linesplit[5])}
        products.append(prod)
        with open("file4.txt", "r") as f:
            rows1 = f.readlines()
            for row1 in rows1:
                fields1 = row1.split(' ')
                cursor.execute(f'INSERT INTO shoes (name, count, brand, size, price)'
                               f"values('{fields1[1]}','{fields1[2]}','{fields1[3]}','{fields1[4]}','{fields1[5]}')")
        connection.commit()


while True:
    num = int(input())
    if num == 1:
        ID = int(input("id: "))
        name = str(input("Название: "))
        count = int(input("Количество: "))
        brand = str(input("Производитель: "))
        size = int(input("Размер: "))
        price = int(input("Цена: "))
        query ='INSERT into shoes (id, name, count, brand, size, price) values(?,?,?,?,?,?)'
        data = [(ID, name, count, brand, size, price)]
        for row in data:
            cursor.execute(query, row)

        connection.commit()

        product = {"id": ID,"name": name, "count": count, "brand": brand, "size": size, "price": price}
        products.append(product)

    elif num == 2:
        print(products)
        cursor.execute('select * from shoes')
        print(cursor.fetchall())

    elif num == 0:
        file = open("save.txt", "w")
        for element in products:
            file.write(str(element) + '\n')
        file.close()
        connection.commit()
        break

    elif num == 3:
        readfile()

    elif num == 4:
        index = int(input())
        del products[index]
        cursor.execute("DELETE FROM shoes WHERE ID = ?", (index,))
        connection.commit()

    elif num == 5:
        data = cursor.execute("SELECT SUM(count) FROM shoes GROUP BY brand")
        for row in data:
            print(row)
        data1 = cursor.execute("SELECT SUM(count) FROM shoes GROUP BY size")
        for row1 in data1:
            print(row1)