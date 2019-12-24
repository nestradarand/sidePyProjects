import pyautogui as auto
import time

BLACKLIST = 'yahoo_blacklist.txt'
###for search bar use x-480 y- 221
def emailToBarFind(sender):
    auto.click(480,221,clicks = 3)
    auto.typewrite('from: ' + sender)
    auto.press('enter')

def selectAll():
    auto.click(444,460)
def hitDelete():
    auto.click(1302,460)
def fullRemove(email):
    emailToBarFind(email)
    time.sleep(2)
    selectAll()
    time.sleep(2)
    hitDelete()


def main():
    emails = ['noah.estrada456@gmail.com',
              'estra146@mail.chapman.edu']
    ####opens chrome and gets to yahoo email
    auto.press('winleft')
    auto.typewrite('chrome')
    time.sleep(1)
    auto.press('enter')
    time.sleep(.5)
    auto.click(603,98,clicks = 3)
    auto.typewrite('mail.yahoo.com')
    auto.press('enter')
    time.sleep(2)
    

    ####read in from blacklist
    email_list = [line.rstrip('\n') for line in open(BLACKLIST)]
    if len(email_list) >0:
        for i in range(0,len(email_list)):
            fullRemove(email_list[i])
    else:
        print("No emails in blacklist to remove")

if __name__ == "__main__":
    main()
