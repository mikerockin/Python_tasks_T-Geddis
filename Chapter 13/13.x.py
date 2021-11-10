# -*- coding: utf8 -*-
# Упражнение по программированию 13-8

# Рисунок старого дома

# Эта программа рисует контур дома.
import tkinter

# Именованные константы
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
HOUSE_X = 50
HOUSE_Y = 400
HOUSE_WIDTH = 500
HOUSE_HEIGHT = 200
ROOF_X = HOUSE_X - 25
ROOF_Y = HOUSE_Y - HOUSE_HEIGHT
ROOF_WIDTH = HOUSE_WIDTH + 50
ROOF_HEIGHT = 150
ROOF_APEX_X = ROOF_X + int(ROOF_WIDTH / 2)
ROOF_APEX_Y = ROOF_Y - ROOF_HEIGHT
DOOR_WIDTH = 80
DOOR_HEIGHT = 150
DOOR_X = (HOUSE_X + int(HOUSE_WIDTH / 2)) - (int(DOOR_WIDTH / 2))
DOOR_Y = HOUSE_Y
WINDOW_WIDTH = 100
WINDOW_HEIGHT = 100
WINDOW1_X = (HOUSE_X + int(HOUSE_WIDTH / 4)) - (int(WINDOW_WIDTH / 2))
WINDOW1_Y = HOUSE_Y - 50
WINDOW2_X = (HOUSE_X + (int(HOUSE_WIDTH / 4) * 3)) - (int(WINDOW_WIDTH / 2))
WINDOW2_Y = WINDOW1_Y
SUN_WIDTH = 75
SUN_X = CANVAS_WIDTH - SUN_WIDTH - 20
SUN_Y = SUN_WIDTH + 20


class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=CANVAS_WIDTH,
                                     height=CANVAS_HEIGHT)

        # Нарисовать корпус дома.
        self.canvas.create_rectangle(HOUSE_X, HOUSE_Y, HOUSE_X + HOUSE_WIDTH,
                                     HOUSE_Y - HOUSE_HEIGHT)

        # Нарисовать крышу.
        self.canvas.create_polygon(ROOF_X, ROOF_Y, ROOF_APEX_X, ROOF_APEX_Y,
                                   ROOF_X + ROOF_WIDTH, ROOF_Y,
                                   ROOF_X, ROOF_Y)

        # Нарисовать дверь.
        self.canvas.create_rectangle(DOOR_X, DOOR_Y,
                                     DOOR_X + DOOR_WIDTH, DOOR_Y - DOOR_HEIGHT)

        # Нарисовать окно 1.
        self.canvas.create_rectangle(WINDOW1_X, WINDOW1_Y,
                                     WINDOW1_X + WINDOW_WIDTH,
                                     WINDOW1_Y - WINDOW_HEIGHT)

        # Нарисовать окно 2.
        self.canvas.create_rectangle(WINDOW2_X, WINDOW2_Y,
                                     WINDOW2_X + WINDOW_WIDTH,
                                     WINDOW2_Y - WINDOW_HEIGHT)

        # Нарисовать осолнце.
        self.canvas.create_oval(SUN_X, SUN_Y,
                                SUN_X + SUN_WIDTH, SUN_Y - SUN_WIDTH,
                                fill='yellow')

        # Упаковать холст.
        self.canvas.pack()

        # Запустить главный цикл.
        tkinter.mainloop()


# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
