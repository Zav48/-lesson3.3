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

#создать переменную с иконой. pygame.image.load - метод для загрузки изображения/ ("img/icon.png") это дирректория,где лежит
# изображение
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

    # начинается работа с событиями. ВАЖНО - взаимодействие между объектами (в нашем слусае клики, выстрел по мишени) и выход из игры
    # (нажатие на крестик). цикл будет перебирать все события в игре и сохранять в переменную event.
    # in и дальше прописываю функцию, которая будет брать все наши события и делать из нх коллекци. event - компонент по работе
    # с событиям в pygame. get() - (получить) все события.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # если тип события = QUIT - покинуть.
            runing = False # то переменная runing = false - цикл завершиться.

            #теперь нужны события, которые будут выполняться в игре - клики мышкой.
        if event.type == pygame.MOUSEBUTTONDOWN: # если тип события = (кнопка на мышке нажата) - то событие будет выполняться.
            maus_x, maus_y = pygame.mouse.get_pos() #в pygame есть функции, которые определяют то место куда мы кликнули мышкой.
            # mouse - в pygame есть компонент по работе с мышкой. get_pos() - (получить) координаты мышки и координата x сохраниться
            # в переменную maus_x, а координата y - в переменную maus_y.
            # проверяем координаты мышки: попали или не попали в координаты цели (target_x, target_y, target_wigth, target_height)

            # проверяем попала ли мышка с коодинатрй х (maus_x) в промежуток от target_x до target_x + target_wigth и с координаты y
            # (maus_y) в промежуток от target_y + target_height.
            if target_x < maus_x < target_x + target_wigth and target_y < maus_y < target_y + target_height:

                #следующие строки создают (новые координаты) новую цель, чтобы цель перемещалась, по которой будет вестись стрельба.
                target_x = random.randint(0, SKREEN_WIDTH - target_wigth)
                target_y = random.randint(0, SKREEN_HEIGHT - target_height)

    #теперь нужно отрисовать нашу цель (target_image) в определённых координатах (target_x, target_y). target_image - изображение,
    # а это координаты, на которых оно должно быть отрисовано.(target_x, target_y)
    SKREEN.blit(target_image, (target_x, target_y))

    #чтобы что-то могло происходить нужно обновлять постоянно экран. в pygame всё происходит покадрово и эти кадры должны
    # последовательно отображаться. для этого нужно прописать с отступом в четыре пробела внутри цикла while.
    pygame.display.update()

#закрыть игру
pygame.quit() # closes all pygame modules - закрывает все модули pygame. завершает игру, как только закроется цикл (folse)

#создать ширину и высоту окна. это делается в строчке после pygame.init()