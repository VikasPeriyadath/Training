stu={101:"Ramesh",102:"Remya",103:"Jishnu",104:"Anand"}
sub=[['perl','c','java'],['networking','c++','linux'],['robotics','dynamics'],['microchip','electrical']]
dep=("IT","CS","ME","EE")
depname=('Information Technology','Computer Science','Mechanical Engg.','Electronics Engg.')


def studdtls():
		op=raw_input("View all student Y/N  :")
		if op=="y":
			print ["%s=%s" % (k, v) for k, v in stu.items()]
		else :
			stid=int(input("Enter student ID  :"))
			print stu[stid]

def editstud():
		stid=int(input("Enter student ID want to Add/Edit :"))
		stname=raw_input("Enter student name :")
		stu[stid]=stname
		print stu

def delstud():
		print "Existing students are : ",stu
		stid=int(input("Enter student ID want to Delete :"))
		del stu[stid]
		print "\n\tDeleted..."
		print "Available students are : ",stu

def depdtls():
		print "Available Departments :",dep
		op=raw_input("View Dep full Name ? Y/N  :")
		if op=="y" :
			depid=raw_input("Enter Dep :")
			if depid=="IT" or depid=="it" : print "\t",depname[0]
			elif depid=="CS" or depid=="cs" : print "\t",depname[1]	
			elif depid=="ME" or depid=="me" : print "\t",depname[2]
			elif depid=="EE" or depid=="ee" : print "\t",depname[3]
			else : print "Not a valid dep !"

def viewsub():
	print "Available Departments :",dep
	depid=raw_input("Enter department to view subjects :")
	print "\t\nSubjects belong to "+depid+" are :"
	if depid=="IT" or depid=="it" : print sub[0]
	elif depid=="CS" or depid=="cs" : print sub[1]	
	elif depid=="ME" or depid=="me" : print sub[2]
	elif depid=="EE" or depid=="ee" : print sub[3]
	else : print "Not a valid dep !"

def addsub():
	print "Available Departments :",dep
	depid=raw_input("Enter department to add subjects :")
	subname=raw_input("Enter subject Name :")
	if depid=="IT" or depid=="it" : 
		sub[0].append(subname)
		print "\nCurrent Subjects belongs to "+depid+" are ",sub[0]
	elif depid=="CS" or depid=="cs" : 
		sub[1].append(subname)
		print "\nCurrent Subjects belongs to "+depid+" are ",sub[1]
	elif depid=="ME" or depid=="me" : 
		sub[2].append(subname)
		print "\nCurrent Subjects belongs to "+depid+" are ",sub[2]
	elif depid=="EE" or depid=="ee" : 
		sub[3].append(subname)
		print "\nCurrent Subjects belongs to "+depid+" are ",sub[3]
	else : print "\tNot a valid dep !"


def errhandler ():
   print("Your input has not been recognised")
loop=0
while(loop!=1):
		print "\n----- please choose from following ----- \n 1.Student Details \n 2.Add/Edit Student \n 3.Delete Student"
		print " 4.Department Details \n 5.View Subjects \n 6.Add Subjects \n 7.Exit \n----------------------------------"
		ch=int(input("\nChoice : "))
		print " "
		if ch==1 : studdtls()
		elif ch==2 : editstud()
		elif ch==3 : delstud()
		elif ch==4 : depdtls()
		elif ch==5 : viewsub()
		elif ch==6 : addsub()
		elif ch==7 : break

print "-----------Bye----------"