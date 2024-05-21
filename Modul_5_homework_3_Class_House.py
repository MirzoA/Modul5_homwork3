class House:    #создание класса
    counter = 0 # атрибут на уровне класса

    def __init__(self, floor=10, type_house='кирпичный'):  # инициализация экземпляра, конструктор класса, магический метод или дандер-метод
        #(self, floor=10) - параметры функции
        self.number_of_floors = floor # атрибут экземпляра класса, свойство экземпляра
        House.counter += 1
        self.type_house = type_house

    def up_floor(self, floor=1):   # метод класса
        self.number_of_floors += floor
        print(self.number_of_floors)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.type_house == other.type_house

house1 = House()
print(f'{House.counter = }), {house1.counter = }, {house1.number_of_floors = }')
house2 = House(15)
print(f'{House.counter = }, {house1.counter = }, {house2.counter = }, {house2.number_of_floors = }')
house3 = House(7)
print(f'{House.counter = }, {house1.counter = }, {house3.counter = }, {house3.number_of_floors = }')

house1.counter = 0
house4 = House(7)
print(f'{House.counter = }, {house4.counter = }, {house4.number_of_floors = }')
house5 = House(15)
print(f'{House.counter = }, {house1.counter = }, {house5.counter = }, {house5.number_of_floors = }')
house6 = House(7)
print(f'{House.counter = }, {house1.counter = }, {house6.counter = }, {house6.number_of_floors = }')
house7 = House(7, 'панельный')
print(f'{House.counter = }, {house1.counter = }, {house7.counter = }, {house7.number_of_floors = }')
print(f'{house2 == house5 = }', house2 == house5)
print(f'{house4 == house6 = }', house4 == house6)
print(f'{house4 == house7 = }', house4 == house7)
print(f'{house4 != house6 = }', house4 != house6)
print(f'{house4 != house7 = }', house4 != house7)