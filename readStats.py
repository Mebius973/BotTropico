import cv2
import numpy as np
import pyautogui
import pytesseract

def read_money():
    screenshot = pyautogui.screenshot(region=(231,50,104,15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh)
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_population():
    screenshot = pyautogui.screenshot(region=(366, 49, 55, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_satisfaction():
    screenshot = pyautogui.screenshot(region=(453, 51, 51, 17))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_happinness():
    pyautogui.press("b")
    screenshot = pyautogui.screenshot(region=(877, 461, 32, 14))
    pyautogui.press("ESCAPE")
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

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
    screenshot = pyautogui.screenshot(region=(642, 322, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_communist():
    screenshot = pyautogui.screenshot(region=(932, 322, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_religious():
    screenshot = pyautogui.screenshot(region=(642, 430, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_militarians():
    screenshot = pyautogui.screenshot(region=(932, 430, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_ecologists():
    screenshot = pyautogui.screenshot(region=(642, 461, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_industrialists():
    screenshot = pyautogui.screenshot(region=(932, 461, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_intellectualists():
    screenshot = pyautogui.screenshot(region=(642, 461, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_conservatists():
    screenshot = pyautogui.screenshot(region=(932, 461, 22, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0

def read_time():
    screenshot = pyautogui.screenshot(region=(1800, 50, 100, 15))
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 7 digits')
    digits = "".join(filter(str.isdigit, text))
    return int(digits) if digits != "" else 0