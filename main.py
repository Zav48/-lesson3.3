import pygame

pygame.init() # initialize all imported pygame modules - инициализировать все импортированные модули pygame

#создать ширину и высоту окна.
SKREEN_WIDTH = 800
SKREEN_HEIGHT = 600

#создать переменную, в которой ббудет экран и далее функцию - pygame.display это метод работает с экраном.
# set_mode - метод для создания экрана с определёнными размерами. (SKREEN_WIDTH, SKREEN_HEIGHT) это ширина и высота и это картеж
SKREEN = pygame.display.set_mode((SKREEN_WIDTH, SKREEN_HEIGHT))

#создать название окна. set_caption - метод для названия окна
pygame.display.set_caption("Игра ТИР")

#создать иконку. pygame.image.load - метод для загрузки изображения
icon = pygame.image.load("")

runing = True # boolean variable - логическая переменная - когда нужно будет заверщить игру переменную сделаю = folse
while runing:
    pass # пока что ни чего не делает(пропуск) нужна, чтобы не выходила ошибка

pygame.quit() # closes all pygame modules - закрывает все модули pygame. завершает игру, как только закроется цикл (folse)

#создать ширину и высоту окна. это делается в строчке после pygame.init()



