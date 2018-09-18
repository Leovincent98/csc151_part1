import sqlite3

db = sqlite3.connect("student.db")
cur = db.cursor()

class Student (object):

	def __init__(self, fName, midInit, lName, course, idNum):
		self.fName = fName
		self.midInit = midInit
		self.lName = lName
		self.course = course
		self.idNum = idNum



cur.execute(
	'''
		CREATE TABLE IF NOT EXISTS studentInfo(
			FirstName TEXT,
			MiddleInit TEXT,
			LastName TEXT,
			Id TEXT,
			Course TEXT
		)
	'''
	)
db.commit()

def addStudent():
	repeat = "yes"
	while((repeat == "YES") or (repeat == "yes")):

		idNum = raw_input("Enter ID Number: ")
		fname = raw_input("Enter First Name: ")
		mname = raw_input("Enter Middle Initial: ")
		lname = raw_input("Enter Last Name: ")
		course = raw_input("Enter Course: ")

		student = Student(fname, mname, lname, course, idNum)

		cur.execute("INSERT INTO studentInfo(Firstname, MiddleInit, LastName, Course, Id) VALUES(?,?,?,?,?)", (student.fName, student.midInit, student.lName, student.course, student.idNum))
		db.commit()

		repeat = raw_input("ADD ANOTHER STUDENTS? ")
	if repeat == "no":
		print "\n\n     >>>student has been added successfully<<<"

def deleteStudent():
	repeat = "yes"
	while((repeat == "YES") or (repeat=="yes")):
		idNum = raw_input("Enter ID Number: ")
		cur.execute("DELETE FROM studentInfo WHERE Id = ?" , (idNum,))
		db.commit()
		repeat = raw_input("DELETE ANOTHER STUDENTS? ")
	if repeat == "no":
		print "\n\n     >>>deleted successfully<<<"


def updateStudent():
	select = raw_input("\nEnter the ID Number: ")
	repeat = "yes"
	while((repeat=="YES") or (repeat=="yes")):
		choice = raw_input("\nWhat do you want to update? \n>>>FName\n>>>LName\n>>>MInitial\n>>>Course\n\n>>>")
		if choice == "FName":
			change = raw_input("\nEnter new first name: ")
			db.execute("UPDATE studentInfo set FirstName = ? where Id = ?", (change,select,))
			db.commit()
		elif choice == "LName":
			change = raw_input("\nEnter new last name: ")
			db.execute("UPDATE studentInfo set LastName = ? where Id = ?", (change,select,))
			db.commit()
		elif choice == "MInitial":
			change = raw_input("\nEnter new middle initial: ")
			db.execute("UPDATE studentInfo set MiddleInit= ? where Id = ?", (change,select,))
			db.commit()
		elif choice == "Course":
			change = raw_input("\nEnter new course: ")
			db.execute("UPDATE studentInfo set Course = ? where Id = ?", (change,select,))
			db.commit()

		repeat = raw_input("UPDATE ANOTHER STUDENTS? ")
	if repeat == "no":
		print "\n\n    >>>update saved successfully<<<"


#______________________________________________________________________________________________________________________________

choice = raw_input("Enter Choices [ADD] [DELETE] [UPDATE]: ")


if((choice=="ADD" ) or (choice=="add")):
	addStudent()
elif((choice=="DELETE") or (choice=="delete")):
	deleteStudent()
elif((choice=="UPDATE") or (choice=="update")):
	updateStudent()