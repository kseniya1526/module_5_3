class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return str(f'Название: {self.name}, количество этажей: {self.number_of_floors}')
    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __it__(self,other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self,other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors =self.number_of_floors + value
            return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        if isinstance(value,int):
            self.number_of_floors += value
            return self


home_1 = House('ЖК Эльбрус', 10)
home_2 = House('ЖК Акация', 20)

print(home_1)
print(home_2)

print(home_1 == home_2) #__eg__

home_1 = home_1 +10 #__add__
print(home_1)

print(home_1 == home_2)

home_1 += 10 #__iadd__
print(home_1)

home_2 = 10 + home_2 #__radd__
print(home_2)

print(home_1 > home_2) #__gt__

print(home_1 >= home_2) #__ge__

print(home_1 < home_2) #__it__

print(home_1 <= home_2) #__le__

print(home_1 != home_2) #__ne__
