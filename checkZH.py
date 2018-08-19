import os
import requests
import re
from bs4 import BeautifulSoup
import datetime
import time

def sendEmail():
    # Import smtplib for the actual sending function
    import smtplib
    
    # Import the email modules we'll need
    from email.mime.text import MIMEText
    
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = MIMEText('ZH just updated')
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'ZH just updated'
    msg['From'] = 'xiaojunch@gmail.com'
    msg['To'] = 'xiaojunch@gmail.com'
    
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('mail.google.com')
    s.send_message(msg)
    s.quit()



def checkUpdate():
    page = requests.get('http://book.zongheng.com/book/672340.html')
    soup = BeautifulSoup(page.content,"lxml")
    update = soup.find("div",{"class":"uptime"})
    updateTime = update.find('br').previous_sibling
    
    updateCase1 = re.match(r'\s*·(\d*)分钟前',updateTime)
    updateCase2 = re.match(r'\s*.*刚刚更新',updateTime)
    
    if (updateCase1 or updateCase2):
        return True
    else:
        return False

        
def main():
    startTime = datetime.time(9,0,0)
    endTime = datetime.time(14,25,0)
    
    while (startTime < datetime.datetime.now().time() and endTime > datetime.datetime.now().time()):
        if checkUpdate():
            sendEmail()
            print('ZH just updated, email notification was sent')
            return
        else:
            time.sleep(300)
            print('Waited another 5 minutes')
    
    print('Waited till 14pm, no update yet.')
    
    
if __name__ == '__main__':
    main()
