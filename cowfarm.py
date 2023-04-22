import time
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import random
import pytesseract

global InFight, healUp
upper_green = np.array([0, 255, 0])
lower_green = np.array([0, 200, 0])
upper_red = np.array([255, 0, 255])
lower_red = np.array([200, 0, 200])
last_x, last_y = None, None
cursor_x, cursor_y = pyautogui.position()

threshold = 0.8
InFight = False
healUp1 = False

class Processor:
    def readImage():
        global InFight
        print('readImage Start')
        while not InFight:
            try:
                screen = np.array(ImageGrab.grab())
                rect_w, rect_h = 100, 100
                top_right_rect = np.array([[screen.shape[1] - rect_w, 0], [screen.shape[1], 0], [screen.shape[1], rect_h], [screen.shape[1] - rect_w, rect_h]])
                rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
                mask = cv2.inRange(rgb, lower_red, upper_red)
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if len(contours) > 0:
                    largest_contour = max(contours, key=cv2.contourArea)
                    rect_intersect = cv2.pointPolygonTest(top_right_rect, (int(largest_contour[0][0][0]), int(largest_contour[0][0][1])), False)
                    if rect_intersect >= 0:
                        continue
                    M = cv2.moments(largest_contour)
                    if M["m00"] > 0:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                        offset = random.uniform(-5, 5)
                        target_x = cx + offset
                        target_y = cy
                        pyautogui.moveTo(target_x, target_y, duration=0.2)
                        pyautogui.click()
                        time.sleep(3)
                        break

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)

    def combatcow2():
        global InFight
        x, y, w, h = 0, 0, 200, 100
        threshold_confidence = 50
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        while True:
            screen = np.array(ImageGrab.grab(bbox=(x, y, x + w, y + h)))
            gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            opening = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel, iterations=1)
            text = pytesseract.image_to_string(opening)
            if "Cow" in text and pytesseract.image_to_data(opening, output_type=pytesseract.Output.DICT)['conf'][0] > threshold_confidence:
                print("Cow detected!")
                InFight = True
            else:
                InFight = False
                break

    def combatcow():
        combatcow = cv2.imread('combatcow.png', 0)
        combatcow2 = cv2.imread('combatcow2.png', 0)
        combatcow3 = cv2.imread('combatcow3.png', 0)
        screen = np.array(ImageGrab.grab())
        gs = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        cowcombatloc = cv2.matchTemplate(gs, combatcow, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(cowcombatloc)
        cowcombatloc2 = cv2.matchTemplate(gs, combatcow2, cv2.TM_CCOEFF_NORMED)
        _, max_val2, _, max_loc = cv2.minMaxLoc(cowcombatloc2)
        cowcombatloc3 = cv2.matchTemplate(gs, combatcow3, cv2.TM_CCOEFF_NORMED)
        _, max_val3, _, max_loc = cv2.minMaxLoc(cowcombatloc3)
        while max_val > 0.95 or max_val2 > 0.95 or max_val3 > 0.95:
            print("Combat cow found! Waiting until it's off the screen...")
            time.sleep(3)
            return True
        else:
            print('No more combat cow.')
            return False

    def healUp():
        print('checking heals')
        lobster = cv2.imread('lobster.png', cv2.IMREAD_COLOR)
        upper_blue = np.array([255, 0, 0])
        lower_blue = np.array([150, 0, 0])
        screen = np.array(ImageGrab.grab())
        rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
        mask = cv2.inRange(rgb, lower_blue, upper_blue)
        lob_result = cv2.matchTemplate(rgb, lobster, cv2.TM_CCOEFF_NORMED)
        if lob_result.size == 0:
            return False
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(lob_result)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0 and (mask.sum() / 255) / mask.size > 0.2:
            if max_val > 0.95:
                target_x, target_y = max_loc[0] + lobster.shape[1] / 2, max_loc[1] + lobster.shape[0] / 2
                pyautogui.moveTo(target_x, target_y, duration=0.2)
                pyautogui.click()
                print('Eating lobster.')
                return True
            else:
                print('No more food.')
                return False

if __name__ == '__main__':
    while True:
        Processor.healUp()
        if InFight == False:
            print('notInFight')
            Processor.readImage()
        if Processor.combatcow() == True:
            InFight == True
            print('InFight')
        if Processor.combatcow() == False:
            InFight = False
            continue



