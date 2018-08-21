import random
import urllib2
import time
from datetime import date
from os import path

phrase = ['come in handy', 'tailored for']
fileThat = hasFunctions = ['class', 'module']

print random.randint(0, 1)
print random.random()
print random.choice(phrase + fileThat)
print urllib2.urlopen("http://g.co").read(20)
print str(time.time()) + ' is the current time from the UNIX epoch in seconds'
print time.gmtime(0)
print date.fromtimestamp(time.time()).strftime('%y/%m/%d')
print date.fromtimestamp(time.time()).isoformat()
print str(path.exists('/Users/pp/Code'))
print path.join('c:', 'windows') + ' by path.join(), designed for cross platforms'
