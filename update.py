import os
import sys
from time import sleep

print '''    _____                          _____       _       _ _   
  / ____|                        / ____|     | |     (_) |  
 | (___  _   _ _ __   ___ _ __  | (___  _ __ | | ___  _| |_ 
  \___ \| | | | '_ \ / _ \ '__|  \___ \| '_ \| |/ _ \| | __|
  ____) | |_| | |_) |  __/ |     ____) | |_) | | (_) | | |_ 
 |_____/ \__,_| .__/ \___|_|    |_____/| .__/|_|\___/|_|\__|
              | |                      | |                  
              |_|                      |_|                  
       Update the Tool | Sam Junior - Telegram: @un00mz
'''

op1 = raw_input( "\nDo You want start the update ? (y/n) -> ")

def update():
	print "\nLet's Go"
	print "Updating..."
	sleep(6)
	os.system('cd ..')
	os.system('git clone https://github.com/UniversalHacking/SuperSploit')
	print "[*]Update Complete [*]"
	sys.exit()

def cancel():
	print "\nExiting..."
	sleep(2)
	print "Bye ^_^"
	sys.exit
if op1 == 'Y':
	update()
if op1 == 'y':
	update()
if op1 == 'n':
	cancel()
if op1 == 'N':
	cancel()
