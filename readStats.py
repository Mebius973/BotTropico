import cv2
import numpy as np
import pyautogui
import pytesseract

def read_number(region):
    screenshot = pyautogui.screenshot(region=region)
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_money():
    return read_number(region=(231,50,104,15))

def read_population():
    return read_number(region=(366, 49, 55, 15))

def read_satisfaction():
    return read_number(region=(453, 51, 51, 17))

def read_happinness():
    pyautogui.press("b")
    result = read_number(region=(877, 461, 32, 14))
    pyautogui.press("ESCAPE")
    return result

def read_population():
    return read_number(region=(366, 49, 55, 15))

def read_satisfaction():
    return read_number(region=(453, 51, 51, 17))

def read_happinness():
    pyautogui.press("b")
    result = read_number(region=(877, 461, 32, 14))
    pyautogui.press("ESCAPE")
    return result

def read_happinness():
    pyautogui.press("b")
    result = read_number(region=(877, 461, 32, 14))
    pyautogui.press("ESCAPE")
    return result

def open_political_menu():
    pyautogui.press("2")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    return

def read_political():
    open_political_menu()
    capitalist = read_capitalist()
    communist = read_communist()
    religious = read_religious()
    militarians = read_militarians()
    ecologists = read_ecologists()
    industrialists = read_industrialists()
    intellectualists = read_intellectualists()
    conservatists = read_conservatists()
    pyautogui.press("ESCAPE")
    
    return [capitalist,
            communist,
            religious,
            militarians,
            ecologists,
            industrialists,
            intellectualists,
            conservatists]


def read_capitalist():
    return read_number(region=(642, 322, 22, 15))

def read_communist():
    return read_number(region=(932, 322, 22, 15))

def read_religious():
    return read_number(region=(642, 430, 22, 15))

def read_militarians():
    return read_number(region=(932, 430, 22, 15))

def read_ecologists():
    return read_number(region=(642, 461, 22, 15))

def read_industrialists():
    return read_number(region=(932, 461, 22, 15))

def read_intellectualists():
    return read_number(region=(642, 492, 22, 15))

def read_conservatists():
    return read_number(region=(932, 492, 22, 15))

def read_communist():
    return read_number(region=(932, 322, 22, 15))

def read_religious():
    return read_number(region=(642, 430, 22, 15))

def read_militarians():
    return read_number(region=(932, 430, 22, 15))

def read_ecologists():
    return read_number(region=(642, 461, 22, 15))

def read_industrialists():
    return read_number(region=(932, 461, 22, 15))

def read_intellectualists():
    return read_number(region=(642, 492, 22, 15))

def read_conservatists():
    return read_number(region=(932, 492, 22, 15))

def read_religious():
    return read_number(region=(642, 430, 22, 15))

def read_militarians():
    return read_number(region=(932, 430, 22, 15))

def read_ecologists():
    return read_number(region=(642, 461, 22, 15))

def read_industrialists():
    return read_number(region=(932, 461, 22, 15))

def read_intellectualists():
    return read_number(region=(642, 492, 22, 15))

def read_conservatists():
    return read_number(region=(932, 492, 22, 15))

def read_conservatists():
    return read_number(region=(932, 492, 22, 15))

def read_housing():
    return read_number((905,470,60,30))

def read_food():
    return read_number((905,330,60,30))

def read_industry():
    return read_number((905,380,60,30))

def read_tourism():
    return read_number((905,650,60,30))