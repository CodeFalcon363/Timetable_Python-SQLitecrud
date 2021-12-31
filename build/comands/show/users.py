"""
======================
User Displaying
======================
This module is responsible for displaying users from database
If current user has no preveleges, nothing is shown

@param item_data{}

"""


#Permissions

from build.users.security import permissions as user_permission

#Item table fields

from build.core.inputs import items

#Error displays

from vendor.views.core import error_prompt as error_displays

#Shell display messages

from vendor.views.core import shell_prompts as shell_displays

#When displaying item profile data
#We will use views from this folder

from vendor.views.actions.show import users as user_show

#We will use this to create item_data{}
#This value will be passed to the rendor function to display item profile
#This is for users table structure

from configs.database.structures import users as item_table

#User profile 
from build.core.controllers import users as user_controller

#Sessions profile
from build.core.controllers import sessions as session_controller

#Modules profile
from build.core.controllers import modules as module_controller

#Room profile
from build.core.controllers import rooms as room_controller



#Display module data views
from vendor.views.actions.show import modules as modules_views

#Display session data views
from vendor.views.actions.show import sessions as sessions_views


"""
======================
Item Display Method
======================

This is method called when displaying data

"""
def boot(userid, cmd):
	#Permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'disp')
	#Permission
	perm = user_permission.check_permission(userid)
	#Validate comand arguments
	if len(cmd) < 3:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return

	#Check scope to search user with
	raw_keyw = cmd[2].split()
	#Validation
	if len(raw_keyw) < 2:
		shell_displays.invalid_args(cmd[0])
		return

	keyw = raw_keyw[1]
	#Check field to search in 
	raw_field = raw_keyw[0]
	filed_lists = items.item_fields[cmd[1]]
	#Validation
	if raw_field in filed_lists:
		pass
		field = filed_lists[raw_field]
	else:
		shell_displays.invalid_args(cmd[0])
		return

	"""
	=====================
	Display User Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search user with
	Display user from table using keyw as search using the selected field

	"""

	print("Searching for user with " + field + " " + keyw)
	#Check wether user is found!
	user_row = user_controller.get_profile(keyw)
	#Is user found!???
	if user_row == False:
		print(error_displays.no_account)
		return


	#User is found!

	user_id = user_row[0]
	#Load profile display view

	"""
	=================
	Create Item Profile
	=================

	"""
	profile_field = item_table.table_structure
	new_profile = {}
	#Loop through the table fields
	for i in profile_field:
		#Assign value if field exists in the sql row
		new_user_row = user_row
		if profile_field[i] < len(new_user_row):
			#Field found
			#Assing value
			new_profile[i] = new_user_row[profile_field[i]]
		else:
			print(error_displays.table_field_not_found)
		
	#End loop!

	"""
	==========================
	Create User Modules Profile
	==========================
	We will fetch all module associated with the user,
	The show method will determin how to display these data
	Based on account type of the user we are displaying profile data for
	"""

	#Check wether there is a course for this user!

	user_courses_row = user_controller.get_courses(user_id)
	#Check wether user has any sessions [Only loaded if user is staff]
	user_sessions_row = user_controller.get_sessions(user_id)

	#Render name and email
	user_show.rendor(new_profile)

	#Wether user is staff ./If so, load sessions
	if (new_profile['account'] == "staff") and not (isinstance(user_sessions_row, str)) and user_sessions_row != False:
		for i in user_sessions_row:
			module = i[6]
			module_row = module_controller.get_modules(module)[0]
			#Display module sessions
			if (module_row != False) and not isinstance(module_row, str):
				#Found modules for the course
				print("\n")
				#Week day
				sessions_views.rendor(["day", i[2]])
				#Module name
				modules_views.rendor(['name', module_row[1]])
				#Start time
				sessions_views.rendor(["start_time", i[3]])
				#End time
				sessions_views.rendor(["end_time", i[4]])
				#Duration
				sessions_views.rendor(["duration", i[3].split(":"), i[4].split(":")])
				#Category
				sessions_views.rendor(['category', i[8]])
				
				
			else:
				if module_row == False:
					print("Error loading module data...")

			room_row = room_controller.get_room(i[5])
			#Room name
			sessions_views.rendor(["room", room_row[1]])
		#Finished printing results!
		print("Finished with " + str(len(user_sessions_row)) + " sessions...")
			

		return

	#Render course profiles
	if (user_courses_row != False) and not isinstance(user_courses_row, str):
		#Found courses!
		for i in user_courses_row:
			#Course modules
			#Filter by course using course id
			modules_row = module_controller.get_modules(i[2], "course")
			#Check if course has any modules
			if len(modules_row) > 0:
				for i in modules_row:
					#Load module sessions
					session_rows = session_controller.module_sessions(i[0])[0]

					#Session data
					module_row = i
					#Display module sessions
					if (module_row != False) and not isinstance(module_row, str):
						#Found modules for the course
						print("\n")
						#Week day
						sessions_views.rendor(["day", session_rows[2]])
						#Module name
						modules_views.rendor(['name', module_row[1]])
						#Start time
						sessions_views.rendor(["start_time", session_rows[3]])
						#End time
						sessions_views.rendor(["end_time", session_rows[4]])
						#Duration
						sessions_views.rendor(["duration", session_rows[3].split(":"), session_rows[4].split(":")])
						#Category
						sessions_views.rendor(['category', session_rows[8]])
						
						
					else:
						if row == False:
							print("Error loading module data...")

					room_row = room_controller.get_room(session_rows[5])
					#Room name
					sessions_views.rendor(["room", room_row[1]])
	else:
		#Check wether nothing is found!
		if user_courses_row == False:
			print(error_displays.no_course)







