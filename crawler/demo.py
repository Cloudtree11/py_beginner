
import urllib2
import cookielib

'''response = urllib2.urlopen('http://www.baidu.com')

print response.headers

html = response.read()
f = open('content.html', 'w')
f.write(html)
f.close()'''

url = 'http://www.baidu.com'

response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(request)
print response3.getcode()
print cj
#print response3.read()

