from mimesis import Person
from mimesis.enums import Gender
from mimesis import Text
import sys
from ui import Ui_NPC_Generator
from PyQt5 import QtCore, QtGui, QtWidgets


def init_app():
    """Функция инициализации приложения"""
    # Create application - инициализация приложения:
    app = QtWidgets.QApplication(sys.argv)
    # Create form and init UI - инициализация формы:
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_NPC_Generator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Run main loop:
    sys.exit(app.exec_())


def test():
    text = Text('ru')
    print(text.swear_word())
    print(text.answer())
    print(text.level())
    print(text.word())

    person = Person('ru')  # сы создали объект person, класса Person()

    man = person.full_name(gender=Gender.FEMALE)
    woman = person.full_name(gender=Gender.MALE)
    age = person.age(minimum=16, maximum=66)
    height = person.height(minimum=1.5, maximum=2.0)
    weight = person.weight(minimum=38, maximum=90)
    sexual_orientation = person.sexual_orientation(symbol=False)
    worldview = person.worldview()
    political_views = person.political_views()

    print(man, woman)
    print(age)
    print(height)
    print(weight)
    print(sexual_orientation)
    print(worldview)
    print(political_views)


def main():  # тут кнопки
    pass



if __name__ == '__main__':
    #init_app()
    #main()
    #test()

