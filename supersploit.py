import os
import sys
from time import sleep
from menu import *

print '''    _____                          _____       _       _ _   
  / ____|                        / ____|     | |     (_) |  
 | (___  _   _ _ __   ___ _ __  | (___  _ __ | | ___  _| |_ 
  \___ \| | | | '_ \ / _ \ '__|  \___ \| '_ \| |/ _ \| | __|
  ____) | |_| | |_) |  __/ |     ____) | |_) | | (_) | | |_ 
 |_____/ \__,_| .__/ \___|_|    |_____/| .__/|_|\___/|_|\__|
              | |                      | |                  
              |_|                      |_|                  
 AutoExploit Tool and Exploit Search | Sam Junior - Telegram: @un00mz
'''

def help():
	print "\nCommands"
	print "========="
	print "show exploits menu"
	print "use exploit search"
	print "open <menu_name>"
	print "update"
	print "exit"

def exploits_menu():
	print "\nExploits Menu"
	print "=============="
	print "ftp"
	print "ssh"
	print "openssl"
	print "telnet"

def enter():
	enter = raw_input("Press Enter to Continue ...")
	os.system('reset')
	os.system('sudo python supersploit.py')

print "[!] Run: help [!]"
select = raw_input("\nsSploit> ")
if select == 'help':
	help()
	enter()
elif select == 'show exploits menu':
	exploits_menu()
	enter()
elif select == 'open ftp':
	print menu_ftp()
elif select == 'open ssh':
	print menu_ssh()
elif select == 'open openssl':
	print menu_openssl()
elif select == 'open telnet':
	print "Building"
elif select == 4:
	print "\nExiting..."
	sleep(2)
	print "Bye !"
	sys.exit()
else:
	os.system('reset && sudo python supersploit.py')
