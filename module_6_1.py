"""
Задача "Съедобное, несъедобное":
Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды... Почему бы и нам не попробовать
выстроить что-то подобное используя наследования классов? Необходимо описать пример иерархии животного мира, используя
классы и принцип наследования.
Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого
животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
4 класса наследника:
Mammal, Predator - для Animal и Flower, Fruit - для Plant.
У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут
fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется
атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
