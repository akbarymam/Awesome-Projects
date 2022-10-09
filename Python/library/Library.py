from datetime import datetime
class library:
	
	def __init__(self,name):
		self.name=name
	
	def person(self):
		return f"WHAT DO YOU WANT {self.name}?\n"

	def log_now(self,msg):
		with open("lend_book.txt", "a") as f:
			f.write(f"{self.name} borrowed the book {msg} on {datetime.now()}\n")
			f.close()
		
	def log_add(self,msg):
		with open("add_book.txt", "a") as f:
			f.write(f"{self.name} added the book {msg} on {datetime.now()}\n")
			f.close()
	
	def log_show():
		with open("show_book.txt") as f:
			for i in f:
				print(i)
			f.close()
	
	def log_display(buk):
		with open("show_book.txt", "a") as f:
			f.write(f"{buk}\n")
			f.close()
		
	def log_return(self,msg):
		with open("return_book.txt", "a") as f:
			f.write(f"{self.name} returned the book {msg} on {datetime.now()}\n")
			f.close()

print("\nWELCOME TO THE LIBRARY\n")
print("WHAT IS YOUR NAME?")
b=input()
b=library(b)
print(b.person())
print("1)DISPLAY BOOKS.\n2)LEND BOOK.\n3)ADD BOOK.\n4)RETURN BOOK.\n")
a=int(input())


i=0
while True:
	
	if a==1:
		library.log_show()
		break
		
	elif a==2:
		p=input("CHOOSE THE BOOK YOU WANT TO BORROW:\n")
		library.log_now(b,p)
		print("DO YOU WANT TO BORROW MORE BOOKS: y/n")
		z=input()
		if z =="n":
			break
		else:
			continue
		
	elif a==3:
		x=input("ENTER THE BOOK YOU WANT TO ADD:\n")
		library.log_add(b,x)
		library.log_display(x)
		print("DO YOU WANT TO ADD MORE: y/n")
		z=input()
		if z =="n":
			break
		else:
			continue
	
	elif a==4:
		l=input("ENTER THE BOOK YOU WANT TO RETURN:\n")
		library.log_return(b,l)
		print("DO YOU WANT TO RETURN MORE: y/n")
		z=input()
		if z =="n":
			break
		else:
			continue
	else:
		print("ERROR!!!!!!","\n","YOU HAVE ENTERED A WRONG NUMBER")
		break
	
	continue
	
	i+=1
