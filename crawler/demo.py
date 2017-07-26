
import urllib2

response = urllib2.urlopen('http://www.baidu.com')
html = response.read()

print response.headers

f = open('content.html', 'w')
f.write(html)
f.close()
