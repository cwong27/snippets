import sys
import re

def testIP():
	print ('Test IP')
	ips = ["10.0.0.1", "127.0.0.1", "10.0.10.127", "192.0.73.12", "123.0.0.1", "14.1.91.11"]
	pattern = "(10|127|192)(.)\\d{1,}(.)\\d{1,}(.)\\d{1,}"
	for ip in ips:
		if re.match(pattern, ip):
			print (f"Bad ip: {ip}")

def testBadURL():
	print ('Test Bad URL')
	urls = ["http://hello.com", "bad.com", "evil.com", "https://www.evil.com", "good.com", "http://good.com", "sub.evil.com", "https://dom.bad.com"]
	pattern1 = "http://.*"
	pattern2 = ".*(bad|evil)(.com)?"
	for url in urls:
		if re.match(pattern1, url) or re.match(pattern2, url):
			print (f"Bad URL: {url}")

def testGodURL():
	print ('Test good URL')
	urls = ["www.good.com", "www.corp.com", "https://ok.com", "https://www.ok.com", "sub.corp.com", "https://ok.good.com", "www.bad.com"]
	pattern1 = "https://\w*(.)?(ok|good|corp)(.com)?"
	pattern2 = "\w*(.)?(ok|good|corp)(.com)?"
	for url in urls:
		if re.match(pattern1, url) or re.match(pattern2, url):
			print (f"Good URL: {url}")


def main(argv):
	print ('Regex')


	m = re.search('a*','abceaabdfg')
	print (m.group(0))

	print (re.split('\W+', 'Words, words, words.'))

	m = re.search('(?<=abc)def', 'abcdef')
	print (m.group(0))

	testIP()
	testBadURL()
	testGodURL()
	exit()


if __name__ == "__main__":
	main(sys.argv[1:])