import os
import serial
import time
import subprocess
import StringIO

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

	p = subprocess.Popen("ls -la " + keyfolder, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = p.stdout.read()

	#print "program output:", output
	dat = StringIO.StringIO(output)
	data = dat.readline()
	while data:
		#time.sleep(0.005)
		data = dat.readline()
		#if len(data) > 0:
		#	print(CYELLOW + data + CEND),
		if (".txt" in data):
			files.append(data)
			print(data),
	#print("f")
	#print(data)
	#print()
	files = [e[42:-1] for e in files]
	print(files)


def disp():
	global files, rows, columns, selection
	#for y in range(int(rows)):
	#	print(y)
	os.system("clear")
	s = 0
	for name in files:
		print("("),
		if selection == s:
			print("X"),
		else:
			print(" "),
		print(") "),
		print(name)
		s = s + 1



def userinput():
	global selection, run
	data = ser.readline()
	#print(CYELLOW + data + CEND),
	while "hello" not in data:
		time.sleep(0.005)
		data = ser.readline()
		if len(data) > 0:
			#print(CYELLOW + data + CEND),
			if "5" in data:
				#print("down")
				selection = selection + 1
				return()
			if "12" in data:
				#print("up")
				selection = selection - 1
				return()
			if "2" in data:
				run = False
				print("Exiting...")
				#time.sleep(1)
				return()
			if "1" in data:
				selectit()
				ser.close()
				exit()

		#if L:
		#	print("Exiting...")
		#	exit()
		#data = ser.readline()
	return()


def selectit():
	global files, selection, run
	print("Selecting: " + files[selection])
	print("sudo cp -f " + keyfolder + files[selection] + " /boot/wifikeyfile.txt")
	os.system("sudo cp -f " + keyfolder + files[selection] + " /boot/wifikeyfile.txt")
	run = False

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
	#print(run)
	time.sleep(0.3)

	time.sleep(refreshrate)

ser.close()
exit()
