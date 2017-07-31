
# coding=UTF-8

import urllib2, cookielib, re, time

def get_http_response(url):
    '''Get http response method

    '''

    # First method
    #response1 = urllib2.urlopen(url)
    #print response1.getcode()
    #print len(response1.read())

    # Second method
    request = urllib2.Request(url)
    request.add_header("user-agent", "Mozilla/5.0")
    response = urllib2.urlopen(request)
    #print response2.getcode()
    #print len(response2.read())'''

    # Third method
    #cj = cookielib.CookieJar()
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #urllib2.install_opener(opener)
    #response = urllib2.urlopen(request)
    #print "Http return code:", response3.getcode()
    #print "Actual url:", response3.geturl()
    #print "Http return info:\n",response3.info()
    #print "Cookies:\n", cj
    return response

url = 'http://blog.csdn.net/dog250?viewmode=contents'
http_response = get_http_response(url)
html_raw = http_response.read()
#f = open('content.html', 'w')
#f.write(html_raw)
#f.close()
#html_regex = re.compile(r"<a href=\"/dog250/article/details/\d+\">")
html_regex = re.compile(r"\"/dog250/article/details/\d+\">")
links = []

for link in html_regex.findall(html_raw):
    link = link[1:-2]
    link = "http://blog.csdn.net" + link
    #print link
    links.append(link)

for link in links:
    time.sleep(10)
    http_response = get_http_response(link)
    html_raw = http_response.read()
    title_regex = re.compile(r"<title>.+?Netfi", re.S)
    title_match = title_regex.search(html_raw)
    if title_match == None:
        print "title match failed"
    else:
        title = title_match.group()
        title = title[7:-8]
    #with open(file_name, 'w') as f:
    #    f.write(html_raw)
        print title








