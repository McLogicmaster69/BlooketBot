from pydoc import cli
from typing import final
from xml.dom.expatbuilder import ElementInfo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.mouse import Button, Controller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException    
import pyautogui
from pynput.mouse import Button, Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as ky
import time
import os

#################################################
# VARIABLES
#################################################

mouse = Controller()
keyboard = ky()
cardPositions = [(480, 680), (1440, 680), (480, 920), (1440, 920)]
correct = []
money = 0

print("Input text file name of correct answers")
fName = input()

correctFile = open(f"{fName}.txt", "r", encoding = "utf8")
correct = correctFile.read()
correctFile.close()
correct = correct.split("\n")

#################################################
# FUNCTIONS
#################################################

def MoveMouse(pos):
    mouse.position = pos
def Click():
    mouse.click(Button.left, 1)
def msg(txt):
    print(" --> " + txt)
def GetIndexOfCorrect(element):
    i = 1
    while i < len(correct):
        if(correct[i] == element):
            return i - 1
        else:
            i += 2
    return -1
def ElementExists(className):
    try:
        driver.find_element_by_class_name(className)
    except NoSuchElementException:
        return False
    return True

#################################################
# MAIN FUNCTIONS
#################################################

def AnswerQuestion():
    if ElementExists("styles__questionText___2MlSZ-camelCase"):
        question = driver.find_element_by_class_name("styles__questionText___2MlSZ-camelCase")
    else:
        return
    question = question.find_element_by_tag_name("div")
    indexOfCorrect = GetIndexOfCorrect(question.text)
    msg(question.text + ": " + correct[indexOfCorrect])
    answers = driver.find_elements_by_class_name("styles__answerText___2eIBw-camelCase")
    for a in range(len(answers)):
        aDiv = answers[a].find_element_by_tag_name("div")
        if aDiv.text == correct[indexOfCorrect]:
            MoveMouse(cardPositions[a])
            Click()
            break

#################################################
# SETUP
#################################################

PATH = "E:/chromedriver.exe" # <---------------------------- CHANGE TO PATH OF CHROME DRIVER
msg("Initilising bot")

options = webdriver.ChromeOptions()
options.binary_location = PATH
options.add_argument("--log-level=3")
driver = webdriver.Chrome(PATH)
driver.maximize_window()

#################################################
# LOGIN
#################################################

driver.get("https://www.blooket.com/play")

# Join Game
msg("Input code")
code = input()
MoveMouse((930, 650))
Click()
for s in code:
    keyboard.press(s)
    keyboard.release(s)
time.sleep(0.1)
keyboard.press(Key.enter)
time.sleep(2)
#Enter name

print("Input name")
name = input()

for s in name:
    keyboard.press(s)
    keyboard.release(s)
time.sleep(0.1)
keyboard.press(Key.enter)
# Wait
msg("Waiting for start")

#################################################
# Crushing time
#################################################

# Reject the dumb idea of a tutorial
input()
MoveMouse((1050, 630))
Click()

while True:
    if pyautogui.pixel(1110, 630)[0] == 11 and pyautogui.pixel(1110, 630)[1] == 194 and pyautogui.pixel(1110, 630)[2] == 207:
        if(pyautogui.pixel(955, 600)[0] == 255):
            MoveMouse((955, 600))
        elif(pyautogui.pixel(955, 610)[0] == 255):
            MoveMouse((955, 610))
        elif(pyautogui.pixel(955, 620)[0] == 255):
            MoveMouse((955, 620))
        elif(pyautogui.pixel(955, 630)[0] == 255):
            MoveMouse((955, 630))
        elif(pyautogui.pixel(955, 640)[0] == 255):
            MoveMouse((955, 640))
        elif(pyautogui.pixel(955, 650)[0] == 255):
            MoveMouse((955, 650))
        Click()
    elif pyautogui.pixel(69, 420)[0] == 76 and pyautogui.pixel(69, 420)[1] == 194 and pyautogui.pixel(69, 420)[2] == 47:
        Click()
    elif pyautogui.pixel(960, 680)[0] == 255 and pyautogui.pixel(960, 680)[1] == 255 and pyautogui.pixel(960, 680)[2] == 255:
        AnswerQuestion()
    elif ElementExists("styles__playerEnergy___G4cGN-camelCase"):
        m = driver.find_element_by_class_name("styles__playerEnergy___G4cGN-camelCase")
        nm = int(m.text)
        if nm > money:
            Click()
        money = nm
        msg(str(money))

time.sleep(1000)

# styles__questionText___2MlSZ-camelCase
# question
# styles__answerText___2eIBw-camelCase
# answer
# styles__playerEnergy___G4cGN-camelCase
# mone

#################################################
# BEAT FIN
#################################################
#
#MoveMouse((0, 0))
#while pyautogui.pixel(950, 680)[0] != 60:
#    print("Waiting")
#MoveMouse((945, 650))
#Click()
#options = driver.find_elements_by_class_name("MatchModeQuestionGridBoard-tile")
#order = []
#for o in options:
#    no = o.find_element_by_class_name("FormattedText")
#    order.append(no.get_attribute("aria-label"))
#
#
#for ord in range(len(order)):
#    ind = GetIndex(order[ord])
#    match = GetIndexOfOrder(correct[GetMatch(ind)])
#    print(ord)
#    print(match)
#    if match > ord:
#        MoveMouse(cardPositions[ord])
#        Click()
#        MoveMouse(cardPositions[match])
#        Click()
#        time.sleep(0.02)
#
time.sleep(10)
driver.quit()
