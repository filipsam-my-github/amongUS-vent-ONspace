import pynput,win32api
from pynput.keyboard import Key, Listener
import win32con
import time
import win32api,pydirectinput
# keys = []
  
# def on_press(key): 
#     print(key)
#     if Key.char==Key.space:
#         pydirectinput.moveTo(1270,740)
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
#         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
# import win32api
# import win32con
# import time,asyncio

# click_info = {"right": False, "left": False}

# async def click():
#     while True:
#         if click_info["right"]:
#             click_info["right"]=False
#             pydirectinput.moveTo(1270,740)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
#         await asyncio.sleep(0.1)
# import pynput
# import win32api
# import win32con
# import time
# import threading
# import sys

# click_info = {"right": False, "left": False}

# def on_press(key):
#     try:
#         if key.char == "r":
#             click_info["right"] = not click_info["right"]
#     except:
#         pass

# def clicking():
#     while True:
#         if click_info["right"]:
#             print("a")
#             time.sleep(0.05)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#             time.sleep(0.05)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)



# pynput.keyboard.Listener(on_press=on_press).start()

# threading.Thread(target=clicking).start()


# import os
# import pynput
# import win32api
# import win32con
# import threading

# import win32api
# import win32con
# import time
# import threading
# import sys
# from pynput import keyboard

# click_info = {"right": False}

# def on_press(key):
#     try:
#         if key.char == "r":
#             click_info["right"] = not click_info["right"]
#     except AttributeError:
#         pass

# def clicking():
#     while True:
#         if click_info["right"]:
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#             time.sleep(0.05)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#             time.sleep(0.05)

# keyboard.Listener(on_press=on_press).start()

# threading.Thread(target=clicking).start()

import keyboard
import win32api
import win32con
import time
import threading
import sys,pyautogui

click_info = {"space": False}
def on_press(key):
    try:
        if key.name == "space":
            click_info["space"] = True
    except:
        pass

def clicking():
    while True:
        if click_info["space"]:
            click_info["space"]=False
            pydirectinput.moveTo(1570,940)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        else:
            time.sleep(0.01)

keyboard.on_press(on_press)

threading.Thread(target=clicking).start()

  
