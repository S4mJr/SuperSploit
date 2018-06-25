import os

print '''    _____                          _____       _       _ _   
  / ____|                        / ____|     | |     (_) |  
 | (___  _   _ _ __   ___ _ __  | (___  _ __ | | ___  _| |_ 
  \___ \| | | | '_ \ / _ \ '__|  \___ \| '_ \| |/ _ \| | __|
  ____) | |_| | |_) |  __/ |     ____) | |_) | | (_) | | |_ 
 |_____/ \__,_| .__/ \___|_|    |_____/| .__/|_|\___/|_|\__|
              | |                      | |                  
              |_|                      |_|                   
	Exploit Search Tool | Savage - Telegram: @un00mz
'''


print "\n\nExploit-Search\n\n"
os.system("sudo pip install -r requirements.txt")
os.system("clear")
print '''    _____                          _____       _       _ _   
  / ____|                        / ____|     | |     (_) |  
 | (___  _   _ _ __   ___ _ __  | (___  _ __ | | ___  _| |_ 
  \___ \| | | | '_ \ / _ \ '__|  \___ \| '_ \| |/ _ \| | __|
  ____) | |_| | |_) |  __/ |     ____) | |_) | | (_) | | |_ 
 |_____/ \__,_| .__/ \___|_|    |_____/| .__/|_|\___/|_|\__|
              | |                      | |                  
              |_|                      |_|                  
	Exploit Search Tool | Savage: @un00mz
'''

print "Input Word (1)"
print "Back       (2)"
select = input("\nSelect -> ")

if select == 1:
	nome = raw_input("Word > ")
	os.system('python bin/exploit-search/exploit-search.py -s %(nome)s ' % locals())
if select == 2:
	os.system('python supersploit.py')
