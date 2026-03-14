import random
import time

import pyautogui

def random_scroll():
    # scroll horizontal
    pyautogui.keyDown("right")
    time.sleep(random.uniform(0.1,0.5))
    pyautogui.keyUp("right")
    
    # scroll vertical
    pyautogui.keyDown("down")
    time.sleep(random.uniform(0.1,0.5))
    pyautogui.keyUp("down")

def click_on_map():
    visible_x_min, visible_x_max = 0, 1919
    visible_y_min, visible_y_max = 0, 1079
    pyautogui.click(random.randint(visible_x_min, visible_x_max),
                    random.randint(visible_y_min, visible_y_max))

def build_something():
    pyautogui.press("b")
    for _ in range(random.randint(0,12)):
        pyautogui.press("TAB")
    pyautogui.click(random.randint(494,1447),random.randint(222,676))
    random_scroll()
    click_on_map()
