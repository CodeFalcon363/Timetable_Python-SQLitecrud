"""
======================
User Modules Assigning
======================
This module is responsible for creating new user courses records
If current user has no preveleges, nothing is processed
If a course is assigned to the user, all modules under that course will be assigned to the user
Once the course has been removed, all the modules are also removed!

"""

#Permissions
from build.users.security import permissions as user_permission

#User table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Shell clobal options [e.g. q/Q for quit]
from build.core import shell_options as shell_choice

#Time course or module assigned
from datetime import datetime

#To get room id
from build.core.controllers import rooms as room_controller

#Sessions controller file
from build.core.controllers import sessions as session_controller

#User profile and id
from build.core.controllers import users as user_controller

#Module profile and id
from build.core.controllers import modules as module_controller

#Course profile and id
from build.core.controllers import courses as course_controller

"""

"""
def boot(userid, cmd):
	"""


	"""
	if not cmd[2] in ('c'):
		#Invalid comand
		print(error_displays.no_comand)
		return

	print("Assigning items to user...")
	new_cmd = cmd
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'ass')

	#Permission
	perm = user_permission.check_permission(userid)

	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return

	#Validate comand arguments
	if len(new_cmd) < 5:
		#Invalid arguments
		shell_displays.invalid_args(new_cmd[0])
		return

	#Check scope to search user with

	raw_keyw = cmd[3].split()

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

	#Check wether using email or id
	#If not, return error and force email/id
	if not raw_field in ('ui', 'ue'):
		#Invalid user selection!
		print(error_displays.no_account)
		return

	#Check user availability!
	print("Checking user availability...")
	user_row = user_controller.get_profile(keyw)

	#Is user found!???
	if user_row == False:
		print(error_displays.no_account)
		return


	#User is found!
	print("User profile found...")
	new_userid = user_row[0]

	#New user permission
	new_perm = user_permission.check_permission(new_userid)

	#Item validation 
	raw_keyw = cmd[4].split()

	#Validation
	if len(raw_keyw) < 2:
		shell_displays.invalid_args(cmd[0])
		return

	keyw = raw_keyw[1]

	#Check field to search in 

	raw_field = raw_keyw[0]
	filed_lists = items.item_fields[cmd[2]]

	#Validation
	if raw_field in filed_lists:
		pass
		field = filed_lists[raw_field]
	else:
		shell_displays.invalid_args(cmd[0])
		return

	if cmd[2] == 'c':
		#Assigning course to user
		print("Assigning course...")

		#Check scope to search course with
		print("Checking course availability...")

		#Item availability!

		item_rows = course_controller.get_courses(keyw, field)

		#Is course found!???
		if item_rows == False:
			print(error_displays.no_item)
			return
		#Course found!
		print("Course profile found...")
		data_assign = "c"
		data_id = item_rows[0][0]
		print("Starting course assign process...")

	#Assign data
	#We save new record into the user_modules or user_courses table
	if data_assign == "c":
		#Assigning course
		#Save new course data if not found!
		item_rows = user_controller.get_courses(new_userid)

		if item_rows != False:
			#Course already found!
			print(error_displays.item_assigned)
			return
		#Course no exist, add new record!
		date_added = datetime.timestamp(datetime.now())
		#Convert with datetime.fromtimestamp(date_added)
		saved = user_controller.save_course([new_userid, data_id, date_added])
		if saved:
			#Success saving new user course
			print("New data assigned with success...")


