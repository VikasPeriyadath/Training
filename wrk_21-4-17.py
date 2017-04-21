import string
l=[]
d={}
print type(li)
print dir(d)
print string.join("abcdef",',')
print getattr(l, "pop")  
print getattr({}, "clear") 

li=['vikas','vishnu','nithinsoman','kp']
print [elem for elem in li if len(elem) > 5]

a = "first"
b = "second"
print 1 and a or b
print (1 and [a] or [b])[0] 


g = lambda x: x*2  
print g(4)
print (lambda x: x*2)(3) 

s = 'buildConnectionString'
print s.ljust(30,'*') 
print s.ljust(10)