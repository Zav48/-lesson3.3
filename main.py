import pygame
import random

pygame.init() # initialize all imported pygame modules - инициализировать все импортированные модули pygame

#создать ширину и высоту окна.
SKREEN_WIDTH = 800
SKREEN_HEIGHT = 600

#создать переменную, в которой ббудет экран и далее функцию - pygame.display это метод работает с экраном.
# set_mode - метод для создания экрана с определёнными размерами. (SKREEN_WIDTH, SKREEN_HEIGHT) это ширина и высота и это картеж
SKREEN = pygame.display.set_mode((SKREEN_WIDTH, SKREEN_HEIGHT))

#создать название окна (подпись - caption).set_caption - метод для названия окна
pygame.display.set_caption("Игра ТИР")

#создать переменную с иконой. pygame.image.load - метод для загрузки изображения/ ("img/icon.png") это дирректория,где лежит изображение
icon = pygame.image.load("img/icon.png")

#прописать функцию для установить иконку. set_icon(icon) - метод для установки иконки. (icon) это переменная иконки
pygame.display.set_icon(icon)

#содать цель по которой будет вестись стрельба
target_image = pygame.image.load("img/target.png")

#создать ширину и высоту цели. нужно обязательно знать размеры, чтобы не выходить за размеры экрана
target_wigth = 50
target_height = 50

#создать цель по которой будет вестись стрельба.(0, SKREEN_WIDTH - target_wigth) это координаты цели. от 0 до ширины экрана минус
# ширина цели. x и y это координаты цели. берутся от верхнего левого угла
target_x = random.randint(0, SKREEN_WIDTH - target_wigth)
target_y = random.randint(0, SKREEN_HEIGHT - target_height)

#создать 3 цветa заливки цели
color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)



runing = True # boolean variable - логическая переменная - когда нужно будет заверщить игру переменную сделаю = folse
while runing:
    SKREEN.fill(color) # fill - метод для заполнения цветом. SKREEN, color это экран и цвет.

    # начинается работа с событиями. цикл будет перебирать все события в игре и сохранять в переменную
    # event.  in и дальше прописываю функцию, которая будет брать все наши события и делать из нх коллекци. event - компонент по работе
    # с событиям в pygame. get() - (получить) все события.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # если событие = QUIT
            runing = False # то переменная runing = false

pygame.quit() # closes all pygame modules - закрывает все модули pygame. завершает игру, как только закроется цикл (folse)

#создать ширину и высоту окна. это делается в строчке после pygame.init()