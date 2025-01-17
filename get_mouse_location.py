import pyautogui as gui

while True:
    try:
        print(gui.position())
    except KeyboardInterrupt:
        break
