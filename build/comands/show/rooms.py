"""
======================
Course Displaying
======================
This module is responsible for displaying users from database
If current user has no preveleges, nothing is shown

"""

#Permissions
from build.users.security import permissions as user_permission

#User table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Sessions profile
from build.core.controllers import sessions as session_controller

#Modules profile
from build.core.controllers import modules as module_controller

#Room profile
from build.core.controllers import rooms as room_controller

#User profile 
from build.core.controllers import users as user_controller

#Display module data views
from vendor.views.actions.show import modules as modules_views

#Display session data views
from vendor.views.actions.show import sessions as sessions_views

#Display room data views
from vendor.views.actions.show import rooms as room_views


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

	print("Searching " + field + " as " + keyw + " in rooms...")

	#Start searching for room

	room_row = room_controller.get_room(keyw)

	if room_row == False:
		print(error_displays.no_item)
		return

	#Init room
	room_id = room_row[0]

	#Get room sessions
	room_sessions = room_controller.sessions(room_id)

	#Anything found!
	if room_sessions == False:
		return

	#Print results

	#Room Profile
	room_views.rendor(["profile_name", room_row[1]])

	for i in room_sessions:
		#Print session profiles

		#Init moduel category
		module_row = module_controller.get_modules(i[6])
		#Have we got anything???
		if module_row == False:
			#Nothing found!
			module_category = "1"
		if len(module_row) < 1:
			#No results
			module_category = "1"

		#Module category init
		module_row = module_row[0]
		module_category = module_row[2]
		print("\n")
		#Tutor
		sessions_views.rendor(["tutor", user_controller.get_profile(i[1])[1]])
		#Week day
		sessions_views.rendor(["day", i[2]])
		#Module name
		modules_views.rendor(["name", module_row[1]])
		#Start time
		sessions_views.rendor(["start_time", i[3]])
		#End time
		sessions_views.rendor(["end_time", i[4]])
		#Duration
		sessions_views.rendor(["duration", i[3].split(":"), i[4].split(":")])

		#Category
		modules_views.rendor(['category', module_category])

	#End displaying module sessions
	print("Finished with " + str(len(room_sessions)) + " session(s)...")







