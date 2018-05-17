#!/usr/bin/env python
import dpkt
import sys
import socket
import math
from dpkt.compat import compat_ord


def processFile(file):

	try:
		f = open(file, 'rb')
	except:
		print "Cannot open input file"
		exit()

	pcap = dpkt.pcap.Reader(f)
	dest_ports = set()
	timestamps = set()
	target_ip = ''

	for timestamp, buf in pcap:
		eth = dpkt.ethernet.Ethernet(buf)

		if not isinstance(eth.data, dpkt.ip.IP):
			print 'Non IP Packet type not supported'
			continue
		
		ip = eth.data

		if isinstance(ip.data, dpkt.tcp.TCP):
			tcp = ip.data
			if tcp.dport == 80:
				continue
			dec, time = math.modf(timestamp)
			dest_ports.add(tcp.dport)
			timestamps.add(time)
			target_ip = socket.inet_ntoa(ip.src)

	f.close()
	sorted_time = sorted(timestamps)
	differences = [sorted_time[i+1]-sorted_time[i] for i in range(len(sorted_time)-1)]
	frequency = max(set(differences), key=differences.count)

	if differences.count(frequency) > 20:
		print '------------------------------------------------------------------'
		print 'Potential DoS attack via HTTP Chunked Transfer Encoding detected: '
		print '------------------------------------------------------------------'
		print 'Targeted IP: ', target_ip
		print 'Numbers of connection to keep opened: ', len(dest_ports)
		print 'Seconds between requests: ', frequency

def main(argv):
	if len(sys.argv) != 2 :
		sys.exit("Usage: ./4.py path/to/input/file/input.pcap")
	selfPath, inputFilePath = sys.argv
	processFile(inputFilePath)

if __name__ == "__main__":
	main(sys.argv[1:])