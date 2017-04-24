try:
    fsock = open("/notthere")       
except IOError:                     
  	print "The file does not exist, exiting gracefully"
  	


import sys                          
print '\n'.join(sys.modules.keys()) 


f=open("nd.py")
print f
print f.read(55)
f.close()
print file("nd.py").read(55)

f2=open("fh/s.txt","w")
f2.write("a demo file this is")
f.close()


f1="fh/s.txt"
file(f1,"a").write("\nadded with append mode")
print file(f1).read()
file(f1).close()


import re

p=re.compile('\d+')
s=p.match("878jhj9")
print s.group()


r = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
s=r.match("vikas.m@gmailcom")
print s.group()


u=re.compile("^[789]\d{9}$")
s=u.match("7086637696")
print s.group()


for i in range(int(raw_input())):
    print "YES" if  re.search(r'^(7|8|9)\d{9}$',raw_input()) else "NO"