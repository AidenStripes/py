#!/usr/bin/python

import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
	try:
		connSkt = socket(AF_INET,SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		connSkt.send('blablaguagua\r\n')
		result = connSkt.recv(100)
		screenLock.acquire()
		print ('%d/tcp open')% tgtPort
		print (str(result))
	except:
		screenLock.acquire()
		print ('%d/tcp closed')%tgtPort
	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost,tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print ("cannot resolve '%s': Unknown host")%tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print ('\n scan results for: ')+ tgtName[0]
	except:
		print ('\n scan result for: ')+ tgtIP
	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPorts)))
		t.start()

def main():
	parser = optparse.OptionParser('usage%prog ' + '-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPorts', type='string', help='specify target port[s] separated by comma')
	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPorts).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print (parser.usage)
		exit(0)
if __name__=='__main__':
	main()