class Cat:
    name = None
    age = None
    color = None

    def __init__(self, name, age, color):
        self.set_data(name, age, color) # Конструктор получает значение
        self.get_data() # Тут он выводит их

    def set_data(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_data(self):
        print(self.name, 'age:', self.age, 'color:', self.color)

cat1 = Cat("Кузя", 7, "Серый")
cat2 = Cat("Чорка", 3, "Черный")
