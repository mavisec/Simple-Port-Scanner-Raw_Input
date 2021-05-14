#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = raw_input("Enter the IP : ")
port = int(raw_input("Enter the port :"))

def port_scanner(port):
	if sock.connect_ex((host,port)):
		print("The %d port is closed") % (port)

	else:
		print("The %d port is open") % (port)

port_scanner(port)