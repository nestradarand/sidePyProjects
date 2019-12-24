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
    time.sleep(.5)
    typeInCMD('docker start compsci')
    time.sleep(3)
    typeInCMD('docker attach compsci')
    openVisualStudio()

if __name__ == '__main__':
    main()

