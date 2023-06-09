import pyautogui
import pywinauto
import pytesseract
import cv2
import numpy as np
from PIL import ImageGrab
import time
import json

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pyautogui._pyautogui_x11 = None
window_title = "RuneLite - steve0001"
app = pywinauto.Application().connect(title=window_title)
window = app.window(title=window_title)
rect = window.rectangle()

def CurrentTile():
    global current_x, current_y, data2
    try:
        with open('live_data.json') as f:
            data = json.load(f)
        world_point = data['worldPoint']
        current_x = world_point['x']
        current_y = world_point['y']
        return current_x, current_y
    except:
        return current_x, current_y

def InventorySpace():
    try:
        with open('live_data.json') as f:
            data = json.load(f)
        inventory = data['inventory']
        for item in inventory:
            if json.dumps(item).startswith('{"index": 27'):
                print('Inven Full')
                return False
        else:
            print('Inven Empty')
            return True
    except:
        return

def Pathing():
    region = (rect.right-160, rect.top+35, rect.right-10, rect.top+100)
    upper_blue = np.array([255, 0, 0])
    lower_blue = np.array([255, 0, 0])
    screenshot = np.array(ImageGrab.grab(bbox=region))
    rgb = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(rgb, lower_blue, upper_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return
    highest_y = float('-inf')

    for contour in contours:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            if cy > highest_y:
                highest_y = cy
                pyautogui.moveTo(cx + region[0], cy + region[1], duration=0.2)
                pyautogui.click()
                time.sleep(2)

def MineCopper():
    upper_red = np.array([255, 0, 255])
    lower_red = np.array([255, 0, 255])
    region = (rect.left, rect.top, rect.right, rect.bottom)
    screenshot = np.array(ImageGrab.grab(bbox=region))
    rgb = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(rgb, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] > 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            pyautogui.moveTo(cx + region[0], cy + region[1], duration=0.2)
            pyautogui.click()
            time.sleep(5)

def BankDeposit():
    deposit = cv2.imread('images/deposit.png', cv2.IMREAD_COLOR)
    upper_red = np.array([0, 0, 255])
    lower_red = np.array([0, 0, 255])
    region = (rect.left, rect.top, rect.right, rect.bottom)
    screen = np.array(ImageGrab.grab(bbox=region))
    rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(rgb, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] > 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            pyautogui.moveTo(cx + region[0], cy + region[1], duration=0.2)
            pyautogui.click()
            time.sleep(4)
            screen = np.array(ImageGrab.grab(bbox=region))
            rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            deposit_result = cv2.matchTemplate(rgb, deposit, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(deposit_result)
            print(max_val)
            if max_val > 0.95:
                target_x, target_y = max_loc[0] + deposit.shape[1] / 2, max_loc[1] + deposit.shape[0] / 2
                print(target_x)
                print(target_y)
                pyautogui.moveTo(target_x + region[0], target_y + region[1], duration=0.2)
                pyautogui.click()
                print('Depositing.')
                InventorySpace() == True
                time.sleep(0.5)
                pyautogui.press("esc")
                return
            else:
                return

def RunEnergy():
    energy = cv2.imread('images/energy.png', cv2.IMREAD_GRAYSCALE)
    energy = cv2.GaussianBlur(energy, (5, 5), 0)
    region = (rect.left, rect.top, rect.right, rect.bottom)
    screen = np.array(ImageGrab.grab(bbox=region))
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    energy_result = cv2.matchTemplate(gray, energy, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(energy_result)
    #cv2.imshow('Screenshot', gray)
    #cv2.imshow('Screenshot2', energy)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    print(max_val)
    if max_val > 0.9:
        target_x, target_y = max_loc[0] + energy.shape[1] / 2, max_loc[1] + energy.shape[0] / 2
        pyautogui.moveTo(target_x + region[0], target_y + region[1], duration=0.2)
        pyautogui.click()
        print('Running.')
        time.sleep(0.5)

if __name__ == '__main__':
    copper_x_range = range(3300, 3304)
    copper_y_range = range(3282, 3285)
    bank_x_range = range(3269, 3272)
    bank_y_range = range(3162, 3173)
    past_mine = range(3286, 3290)
    while True:
        current_x, current_y = CurrentTile()
        if InventorySpace() == True:
            if current_x in bank_x_range and current_y in bank_y_range:
                pyautogui.press("o")
                RunEnergy()
                Pathing()
                if current_x in copper_x_range and current_y in copper_y_range:
                    continue
            elif current_x in copper_x_range and current_y in copper_y_range:
                MineCopper()
                if InventorySpace() == False:
                    pyautogui.press("o")
                    RunEnergy()
                    Pathing()
            elif current_y in past_mine:
                pyautogui.press("p")
                MineCopper()
            else:
                pyautogui.press("o")
                RunEnergy()
                Pathing()
        else:
            if current_x in bank_x_range and current_y in bank_y_range:
                BankDeposit()
            elif current_x in copper_x_range and current_y in copper_y_range:
                pyautogui.press("p")
                RunEnergy()
                Pathing()
            else:
                pyautogui.press("p")
                RunEnergy()
                Pathing()