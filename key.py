from flask import Flask
import pywhatkit as w
import datetime
import pyautogui
import keyboard as k
def mess():

    e = datetime.datetime.now()
    w.sendwhatmsg("+918970453425", " lo", e.hour, (e.minute +1))
    pyautogui.click(1050, 950)
    #time.sleep(2)
    k.press_and_release('enter')
mess()