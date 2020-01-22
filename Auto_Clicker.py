import pyautogui as ui
import time
from PIL import ImageGrab, ImageOps
import keyboard


gameBox = [200, 150, 760, 799]
line = [195, 571, 765, 572]
coordX = [70, 212, 354, 496]

def img_to_grey(line):
    gameImg = ImageGrab.grab(bbox= line)
    gameImg = ImageOps.grayscale(gameImg)
    return gameImg


# def test_time():
#     t1 = time.time()
#     for i in range(100):
#         gameImg = ImageGrab.grab(bbox=gameBox)
#     t2 = time.time()
#     print(t2 - t1)

while True:
    gameImg = img_to_grey(line)
    line[1] -= .04
    line[3] -= .04
    for cord in coordX:
        if gameImg.getpixel((cord, 0)) <= 132:
            ui.click(195 + cord, 572)
    if keyboard.is_pressed('p'):
        break
print('new line is: {}'.format(line))