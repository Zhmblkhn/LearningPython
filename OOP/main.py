class Cat:
    name = None
    age = None
    color = None

    def set_data(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_data(self):
        print(self.name, 'age:', self.age, 'color:', self.color)

cat1 = Cat()
cat1.set_data('Кузя', 6, 'Серый')

cat2 = Cat()
cat2.set_data('Чорка', 3, 'Черный')

cat1.get_data()
cat2.get_data()