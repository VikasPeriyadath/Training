import urllib2, httplib
httplib.HTTPConnection.debuglevel = 1           
request = urllib2.Request(
     'http://diveintomark.org/redir/example301.xml') 
opener = urllib2.build_opener()
f = opener.open(request)
print opener.open(request)



import urllib2, httplib
httplib.HTTPConnection.debuglevel = 1
request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
request.add_header('Accept-encoding', 'gzip')        
opener = urllib2.build_opener()
f = opener.open(request)

compresseddata = f.read()                              
print len(compresseddata)


import StringIO
compressedstream = StringIO.StringIO(compresseddata)   
import gzip
gzipper = gzip.GzipFile(fileobj=compressedstream)      
data = gzipper.read()                                  
print data    

f = opener.open(request)                  
print f.headers.get('Content-Encoding')

import urllib
data = urllib.urlopen('http://diveintomark.org/xml/atom.xml').read()    
print data