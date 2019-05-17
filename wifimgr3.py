import os
import serial
import time
import subprocess
import numpy as np
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    from io import BytesIO
import io
#import six
import tui





refreshrate = 0.01
keyfolder = "/boot/wifikeys/"
files = []
selection = 0
s = 0

CREDBG    = '\33[41m'
CBLUEBG   = '\33[44m'
CEND      = '\33[0m'
CYELLOW = '\33[33m'
CRED    = '\33[31m'

run = True
rows, columns = os.popen('stty size', 'r').read().split()

def filelist():
	global files
	files = []
	p = subprocess.Popen("ls -la " + keyfolder, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = p.stdout.read().decode('utf-8')
	print(output)

	dat = io.StringIO(output)
	#dat = np.genfromtxt(six.StringIO(output))
	data = dat.readline()
	while data:
		data = dat.readline()
		#if len(data) > 0:
		#	print(CYELLOW + data + CEND),
		if (".txt" in data):
			files.append(data)
			print(data),

	files = [e[42:-1] for e in files]
	print(files)


def disp():
	global files, rows, columns, selection
	os.system("clear")
	s = 0
	for name in files:
		print("(", end="")
		if selection == s:
			print("X", end="")
		else:
			print(" ", end="")
		print(") ", end="")
		print(name)
		s = s + 1



def userinput():
	global selection, run
	data = ser.readline()
	#print(CYELLOW + data + CEND),
	while b"hello" not in data:
		time.sleep(0.005)
		data = ser.readline()
		#print(data)
		if len(data) > 0:
			#print(CYELLOW + data + CEND),
			if b"5\r\n" == data: #down
				selection = selection + 1
				return()
			if b"12\r\n" == data: #up
				selection = selection - 1
				return()
			if b"2\r\n" == data: #B
				run = False
				print("Exiting...")
				return()
			if b"1\r\n" == data: #A
				selectit(selection)
				ser.close()
				exit()

			if b"0\r\n" == data: #x
				newfile()
				return()

			if b"3\r\n" == data: #y
				deleteit()
				data=""
				return()


	return()



def deleteit():
	
	print("Deleting in 2 seconds...")
	time.sleep(2)
	os.system("sudo rm " + keyfolder + files[selection])
	filelist()
	disp()

def selectit(selection):
	global files, run
	print("Selecting: " + files[selection])
	print("sudo cp -f " + keyfolder + files[selection] + " /boot/wifikeyfile.txt")
	os.system("sudo cp -f " + keyfolder + files[selection] + " /boot/wifikeyfile.txt")
	run = False

def newfile():
	screensize = tui.getsize()
	ssid = tui.kbdinput("SSID",screensize,"big","",ser)
	pswd = tui.kbdinput("Password",screensize,"big","",ser)
	if len(ssid) > 0:

		f = open(keyfolder + ssid+".txt","w+")
		print('ssid="' + ssid +'"')
		f.write('ssid="' + ssid +'"')
		f.write('\r\n')
		print('psk="' + pswd +'"')
		f.write('psk="' + pswd +'"')
		f.close()
	time.sleep(1)
	filelist()
	disp()




def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

port = 0
#print("Connecting...")
while port == 0:
    for x in range(0, 3):
        try:
            ser = serial.Serial('/dev/ttyACM' + str(x), 115200)
        except serial.SerialException:
            if debug == 1:
                print('Serial Port ACM' + str(x) + ' Not Found')
            time.sleep(0.1)
        else:
            port = 1
            break



filelist()
disp()
#time.sleep(4)

#run = True

while run == True:

	userinput()
	selection = clamp(selection, 0, len(files)-1)
	disp()
	#time.sleep(0.3)

	time.sleep(refreshrate)

ser.close()
exit()
