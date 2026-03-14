import pyautogui
import numpy as np
import cv2

def get_observation():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.resize(frame, (160, 90))
    return frame