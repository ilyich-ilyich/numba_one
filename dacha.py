import time
import datetime
import telepot
import RPi.GPIO as GPIO

def getTemperature():

    filepath='1.txt'
    f=open(filepath,'r')
    data=f.read()
    f.close()
    m =10
    return float (m/10)

def handle(msg):

    chat_id=msg['from']['id']
    command=msg['text']
    if command=='/on':
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7,1)
        GPIO.cleanup()
        bot.sendMessage(chat_id,str('Okey On!'))

    elif command =='/off':
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7,0)
        GPIO.cleanup()
        bot.sendMessage(chat_id,str('Okey Off!'))
    elif command=='/temp':
        bot.sendMessage(chat_id,str(getTemperature())+'C')
    elif command=='/time':
        bot.sendMessage(chat_id,'time now:'+str(datetime.datetime.now()))


    elif command=='/start':
        bot.sendMessage(chat_id,str('Hi! I am homebot!'))
        i=4
bot=telepot.Bot('356276665:AAGaJ6ar6ZUgxDlhgMJ_yJbSxrEnFSM8YkQ')
bot.message_loop(handle)
while 1:
    time.sleep(10)

