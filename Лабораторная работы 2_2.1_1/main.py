# #TODO Написать 3 класса с документацией и аннотацией типов
# import doctest
#
# class Table:
#     __metaclass__=ABCMeta
# if __name__ == "__main__":
#     # TODO работоспособность экземпляров класса проверить с помощью doctest
#     pass
#
# import doctest

# version 1
class Table:
    def __init__(self, object_area: float, occupied_area: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param object_area: Площадь стола
        :param occupied_area: Занимаемая площаль компьютером

        Примеры:
        >>> table = Table(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(object_area, (int, float)):
            raise TypeError("Площадь стола должна быть типа int или float")
        if object_area <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.object_area = object_area

        if not isinstance(occupied_area, (int, float)):
            raise TypeError("Компьютер должен занимать площадь типа int или float")
        if occupied_area < 0:
            raise ValueError("Занимаемая компьютером площадь стола не может быть отрицательным числом")
        self.occupied_area = occupied_area

# version 2
class Bus(Movable):
    def __init__:
        self.speed = 11
        self.x = 0

    def move(self):
        self.x += self.speed

        def speed(self):
            return self.speed


assert issubclass(Bus, Movable)
assert ininstance(Bus(), Movable)

# version 3
class Tree(Object): # опишим класс "дерево"

    def __init__(self, height, age):    # параметры класса дерево

        super().__init__("Tree", 0)
        self.height = height
        self.age = age

    def method1(self):  # действия над "деревом"
        if self.age += self.age:
            self.height += self.height
        pass
