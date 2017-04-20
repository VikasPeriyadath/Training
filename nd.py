dict={"lang1":"android","lang2":"java","lang3":"python"}
print dict
print dict["lang3"]
dict["lang2"]="bootstrap"
print dict
dict["lang4"]="react"
print dict
del dict["lang2"]
print dict


print "LIST"
li=["react","java","android",5]
print li
print li[0]
print li[-1]
print li[1:3]
print li[:3]
print li[3:]
print li[:]
li.append("node")
print li
li.insert(0,'python')
print li
li.extend(['css','sql'])
print li
li.append([1,2])
print li
print len(li)
print li.index("python")