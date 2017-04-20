class dep:
	def getdepdtls(self):
		self.depid=int(input("Enter dep ID :"))
		self.depname=raw_input("Enter dep name :")
	def shwdepdtls(self):
		print "Department ID   : ",self.depid
		print "Department Name : ",self.depname
		

class emp(dep):
	def getempdtls(self):
		self.empid=int(input("Enter  ID  :"))
		self.empname=raw_input("Enter name :")
		self.empadrs=raw_input("Enter adrs :")
		self.empstts=raw_input("Active or not Y/N ? :")
	def shwempdtls(self):
		print "Emp ID   : ",self.empid
		print "Emp Name : ",self.empname
		print "Emp Adrs : ",self.empadrs
		print "Emp Status : ",self.empstts
		
class leave(emp):
	date=[]
	nodays=0
	def applyleave(self):
		self.nodays=int(input("Enter the no of days need leave : "))
		print "Enter dates need leave (dd/mm/yy) : "
		for i in range(0,self.nodays):
			self.d=raw_input()
			self.date.insert(i,self.d)

	def shwleave(self):
		if self.nodays==0 :
				print "\t\tNo leaves are applied "
		else :
			print "no days applied :",self.nodays
			print "Dates are applied   :"
			for i in range(0,self.nodays):
					print "\t \t \t",self.date[i]
		
	

ob=leave()
ob.getempdtls()
ob.getdepdtls()
def errhandler ():
   print("Your input has not been recognised")
loop=0
while(loop!=1):
	case={
	      1: ob.shwempdtls,
	      2: ob.shwdepdtls,
	      3: ob.applyleave,
	      4: ob.shwleave,
	     }

	print "-----please choose from following----- \n 1.Emp dtls \n 2.Dep dtls \n 3.apply leave \n 4.View leave \n 5.Exit"
	ch=int(input())
	if ch==5 :
		break
	case.get(ch,errhandler)()

print "----Bye-----"
	
	

