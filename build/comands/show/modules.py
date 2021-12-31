"""
======================
Course Displaying
======================
This module is responsible for displaying users from database
If current user has no preveleges, nothing is shown

"""

#Database
import config

#Permissions
from build.users.security import permissions as user_permission

#User table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#When displaying item profile data
#We will use views from this folder

from vendor.views.actions.show import modules as module_show

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

#User profile 
from build.core.controllers import users as user_controller


"""

"""
def boot(userid, cmd):
	#Permissions
	allow = user_permission.allowed(user_permission.check_permission(userid))

	#Validate comand arguments
	if len(cmd) < 3:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return 1
	
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Check scope to search user with

	raw_keyw = cmd[2].split()

	#Validation
	if len(raw_keyw) < 2:
		shell_displays.invalid_args(cmd[0])
		return 1

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
		return 1

	"""
	=====================
	Display User Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search user with
	Display user from table using keyw as search using the selected field

	"""

	print("Searching for " + keyw + " as " + field + " in modules...")

	module_row = module_controller.get_modules(keyw, field)
	#Have we got anything???
	if module_row == False:
		#Nothing found!
		print(error_displays.no_item)
		return
	if len(module_row) < 1:
		#No results
		print(error_displays.no_item)
		return

	#Init module_row
	module_row = module_row[0]

	#Module name
	modules_views.rendor(["profile_name", module_row[1]])

	#Display Sessions...
	module_sessions = session_controller.module_sessions(module_row[0])

	if module_sessions == False:
		#Nothing found!
		print(error_displays.no_session)
		return
	if len(module_sessions) < 1:
		#No results
		print(error_displays.no_session)
		return

	for i in module_sessions:
		#Print session profiles
		print("\n")
		#Tutor
		sessions_views.rendor(["tutor", user_controller.get_profile(i[1])[1]])
		#Start time
		sessions_views.rendor(["start_time", i[3]])
		#End time
		sessions_views.rendor(["end_time", i[4]])
		#Duration
		sessions_views.rendor(["duration", i[3].split(":"), i[4].split(":")])
		#Week day
		sessions_views.rendor(["day", i[2]])
		#Category
		modules_views.rendor(['category', module_row[2]])
		#Room
		room_row = room_controller.get_room(i[5])
		#Room name
		sessions_views.rendor(["room", room_row[1]])

	#End displaying module sessions
	print("Finished with " + str(len(module_sessions)) + " session(s)...")


	







