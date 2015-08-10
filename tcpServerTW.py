#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 20000

class TSServerProtocol(protocol.Protocol):
	def connectionMade(self):
		clnt = self.clnt = self.transport.getPeer().host
		print '...connected from:', clnt
	def dataReceived(self, data):
		self.transport.write('(%s) %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServerProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()
