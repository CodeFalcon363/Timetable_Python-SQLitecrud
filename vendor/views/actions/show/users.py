"""
======================
User Profile View
======================

When showing user profile data,
we will use this view to render the profile data

@param user_data{} => user profile data
"""

#Error displays
from vendor.views.core import error_prompt as error_displays



def rendor(user_data):
	#Display user profile
	print("-" * 50)
	guess_name(user_data['account'], user_data['name'], user_data['email'])

	#Last line to indicate user profile display end!
	print("-" * 50)



"""
This method is for displaying user name
We will guess the user type and display appropriate account title
"""

def guess_name(account, name, email):
	#Check account type
	account_title = "Uknown"

	#Rendor name view

	if account == "admin":
		print("""Admin:				         """ + str(name))
	elif account == "student":
		print("""Student:				""" + str(name))
	elif account == "staff":
		print("""Staff:				             """ + str(name))

	#User email address
	print("""Email:				           """ + str(email))


"""
This method is for displaying user modules
We will guess the user account type to display the data in appropriate way

"""

def guess_modules(user_modules):
	#Database init
	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Print modules list if any!
	if len(user_modules) < 1:
		#No modules!
		return
	module_id = user_modules[0]
	sql = "SELECT * FROM sessions WHERE module=?"

	cur.execute(sql, [module_id])

	module_row = cur.fetchall()

	if len(module_row) < 1:
		return

	#Print module data
	print("Loading module sessions...")


def load_module(user_modules):
	#Load modules data...
	print("\n")
	print("""Day:					     """ + str(user_modules[5]))
	print("""Module:				        """ + str(user_modules[1]))
	print("""Start Time:			     """ + str(user_modules[3]))
	print("""End Time:		             """ + str(user_modules[4]))
	print("""Duration:			       """ + str(user_modules[1]))
	print("""Event Category:		       """ + str(guess_category(user_modules[6])))
	print("""Room:				          """ + str(guess_room(user_modules[7])))


"""
This method is for displaying user modules under their courses
We will guess the user account type to display the data in appropriate way

"""

def guess_courses(user_courses):
	#Print course modules list if any!
	#Database init
	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	if len(user_courses) < 1:
		#No courses!
		return

	#Load course modules data...

	for i in user_courses:
		#Load course modules!
		course_id = i[2]

		#Return current course modules
		sql = "SELECT * FROM modules WHERE id=?"

		cur.execute(sql, [course_id])

		course_row = cur.fetchall()

		if len(course_row) > 0:
			#Modules found!
			for i in course_row:
				guess_modules(i)
		else:
			print("No modules found for this course!")
		

"""
This method is for returning wether a module is on campus or off campus

"""

def guess_category(category):
	#Run check
	if category == 1:
		return "On Campus Workshop"
	else:
		return "Off Campus Workshop"


"""
This method is for returning room name

"""

def guess_room(roomid):
	#Database init
	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Run check room
	sql = "SELECT name FROM rooms WHERE id=?"

	cur.execute(sql, [roomid])

	room_row = cur.fetchall()

	if len(room_row) > 0:
		#Found!
		return room_row[0][0]
	#No room data found!
	return "Uknown"


"""
This method is for displaying staff modules weekly

"""

def staff_modules(module_row):

	if len(module_row) > 0:
		#Found!
		for i in module_row:
			guess_modules(i)

		return

	#Nothing found!
	print(error_displays.no_item)