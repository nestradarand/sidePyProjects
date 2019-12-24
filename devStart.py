import pyautogui as auto 
import time
import sys

def openCmd():
    auto.keyDown('winleft')
    auto.keyDown('r')
    auto.keyUp('winleft')
    auto.keyUp('r')
    auto.press('enter')
def openVisualStudio():
    auto.press('winleft')
    time.sleep(.5)
    auto.typewrite('visual')
    auto.press('enter')
def typeInCMD(text):
    auto.click(812,744)
    auto.typewrite(text)
    auto.press('enter')

def main():

    openCmd()
    typeInCMD('cd Desktop/sidePyProjects')
    time.sleep(1)
    openVisualStudio()

if __name__ == '__main__':
    main()

