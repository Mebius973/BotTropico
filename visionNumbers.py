import cv2
import numpy as np
import pyautogui

templates = {}

for i in range(10):
    templates[i] = cv2.imread(f"digits/{i}.png",0)

def read_number_cv(region):

    screenshot = pyautogui.screenshot(region=region)
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

    digits = []

    for digit,template in templates.items():

        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

        loc = np.where(res > 0.85)

        for pt in zip(*loc[::-1]):
            digits.append((pt[0],digit))

    digits.sort()

    number = "".join(str(d[1]) for d in digits)

    if number == "":
        return 0

    return int(number)