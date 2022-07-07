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
        product = {"id": int(linesplit[0]),
                   "name": str(linesplit[1]),
                   "count": int(linesplit[2]),
                   "brand": str(linesplit[3]),
                   "size": int(linesplit[4]),
                   "price": int(linesplit[5])}
        products.append(product)


readfileonstart()

while True:
    num = int(input())

    if num == 4:
        for key, value in dict(products).items():
            if value == int(input()):
                del mydict[key]

    elif num == 2:
        print(products)

    elif num == 0:
        break