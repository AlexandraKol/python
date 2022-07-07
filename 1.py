print('Добро пожаловать!')
print('для добавления нового товара введите 1')
print('для отображения всех товаров введите 2')
print('для ввода товаров из файла введите 3')
print('для удаления товара  введите 4')
print('для вывода статистики введите 5')
print('для выхода введите 0')

products = []

def readfileonstart():
    s = open("file.txt", "r")
    lines = s.readlines()

    for line in lines:
        linesplit = line.split(" ")
        product = {"name": str(linesplit[0]),
                   "count": int(linesplit[1]),
                   "brand": str(linesplit[2]),
                   "size": int(linesplit[3]),
                   "price": int(linesplit[4])}
        products.append(product)

readfileonstart()

def readfile():
    r = open("file.txt", "r")
    lines = r.readlines()

    for line in lines:
       linesplit = line.split(" ")
       product = {"name": str(linesplit[0]),
       "count": int(linesplit[1]),
       "brand": str(linesplit[2]),
       "size": int(linesplit[3]),
       "price": int(linesplit[4])}
       products.append(product)


while True:
    num = int(input())
    if num == 1:
        name = str(input("Название: "))
        count = int(input("Количество: "))
        brand = str(input("Производитель: "))
        size = int(input("Размер: "))
        price = int(input("Цена: "))
        product = {"name": name, "count": count, "brand": brand, "size": size, "price": price}
        products.append(product)
    elif num == 2:
        print(products)
    elif num == 0:
        file = open("save.txt", "w")
        for element in products:
            file.write(str(element) + '\n')
        file.close()
        break
    elif num == 3:
        readfile()
    elif num == 4:
        index = int(input())
        del products[index]
    elif num == 5:
        brands = dict()
        sizes = dict()
        for name in products:
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


        print(sizes)
        print(brands)