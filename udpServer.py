﻿#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = sock(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print 'waiting for message...'
	data, addr = udpSerSock.recvfrom(BUFSIZE)
	udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
	print '...received from and returned to:', addr

udpSerSock.close()	