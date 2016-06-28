import sys
import time
import datetime
import telepot
import subprocess

#Message
def handle(msg):
	
	chat_id = msg['chat']['id']
	
	#Set recieved text as 'command'
	command = msg['text']

	#Prints recieved command
	print 'Got command: %s' % command

	#Messaging '/time' to bot will retrieve date & time with DD/MM/YYYY HH:MM:SS format
	if command == '/time':
		bot.sendMessage(chat_id, str(datetime.datetime.now().strftime("%d/%m/%y/ %H:%M:%S")))

	#'/ip' command retrieves the Raspberry Pi's Local IP through 'ip.py'
	elif command == '/ip':
		eip = subprocess.check_output(['python', '/home/pi/ip.py'])
		bot.sendMessage(chat_id, str(eip))
	
	#'/temp' command retrieves the Raspberry Pi's CPU temperature in Celsius through 'temp.py'
	elif command == '/temp':
		temp = subprocess.check_output(['python', '/home/pi/temp.py'])
		bot.sendMessage(chat_id, str(temp))

	#'/uptime' retrieves the Raspberry Pi's system uptime
	elif command == '/uptime':
		uptime = subprocess.check_output(['uptime'])
		bot.sendMessage(chat_id, str(uptime))

	#'/reboot' Sends message 'Rebooting' and reboots the Raspberry Pi after 10 seconds
	elif command =='/reboot':
		bot.sendMessage(chat_id, 'Rebooting')
		time.sleep(10)
		reboot = subprocess.Popen(['reboot'])		

	#Unrecognizable input returns an error 'Command Not Found.'
	else :
		bot.sendMessage(chat_id, 'Command Not Found.')

#Specific API Key for 'GRCCooler Notification Bot'
bot = telepot.Bot('229149752:AAFAiTniOuKbkAL5HbFguqYBpY_KkRrioYA')
bot.message_loop(handle)

#Prints 'I am Listening ...' on program initiation
print 'I am Listening ...'

#Program runs (checks for commands sent) every 10 seconds.
while 1:
	time.sleep(10)	

