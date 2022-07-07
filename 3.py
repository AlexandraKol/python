print('Добро пожаловать!')
print('для добавления нового товара введите 1')
print('для отображения всех товаров введите 2')
print('для ввода товаров из файла введите 3')
print('для удаления товара  введите 4')
print('для выхода введите 0')


class Database:
    name = 'n/a'
    count = 'n/a'
    brand = 'n/a'
    size = 'n/a'
    price = 'n/a'
    list = []
    copy_list = []

    class Products:
        def __init__(self, name, count, brand, size, price):
            self.name = name
            self.count = count
            self.brand = brand
            self.size = size
            self.price = price

        def __str__(self):
            return "name: %s, count: %s, brand: %s, size: %s, price: %s" % (
            self.name, self.count, self.brand, self.size, self.price)

    def __init__(self):
        self.list = []
        self.copy_list = []

    def addProuct(self, name, count, brand, size, price):
        self.list.append(Database.Products(name, count, brand, size, price))

    def out(self):
        print('\n'.join(str(item) for item in self.list))

    def readfile(self):
        r = open("file.txt", "r")
        lines = r.readlines()

        for line in lines:
            linesplit = line.split(" ")
            product = {"name": str(linesplit[0]),
                       "count": int(linesplit[1]),
                       "brand": str(linesplit[2]),
                       "size": int(linesplit[3]),
                       "price": int(linesplit[4])}
            self.list.append(product)

    def readfileonstart(self):
        s = open("file.txt", "r")
        lines = s.readlines()

        for line in lines:
            linesplit = line.split(" ")
            product = {"name": str(linesplit[0]),
                       "count": int(linesplit[1]),
                       "brand": str(linesplit[2]),
                       "size": int(linesplit[3]),
                       "price": int(linesplit[4])}
            self.list.append(product)

    def savefile(self):
        file = open("save.txt", "w")
        for element in self.list:
            file.write(str(element) + '\n')
        file.close()

    def deletefile(self):
        index = int(input())
        del self.list[index]


d = Database()
d.readfileonstart()

while True:
    num = int(input())
    if num == 1:
        d.addProuct(str(input("Название: ")), int(input("Количество: ")), str(input("Производитель: ")), int(input("Размер: ")), int(input("Цена: ")))

    elif num == 2:
        d.out()

    elif num == 0:
        d.savefile()
        break

    elif num == 3:
        d.readfile()

    elif num == 4:
        d.deletefile()
