"""
===========================
Sessions Profile Display
===========================
This module shows session data

"""

#Permissions
from build.users.security import permissions as user_permission

#Item table fields
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

	#Check scope to search session with

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


	"""

	print("Searching for " + field + " as " + keyw + " in sessions...")

	session_data = session_controller.get_session(keyw)
	#Check wether something is found!
	if session_data != False:
		#Something is found!
		"""

		"""
		i = session_data
		module = session_data[6]
		module_row = module_controller.get_modules(module)
		#Module data...
		if module_row != False:
			module_row = module_row[0]
		else:
			#No module found
			print(error_displays.no_item)
			return
		#Module name
		modules_views.rendor(['profile_name', module_row[1]])
		#Session tutor
		sessions_views.rendor(["tutor", user_controller.get_profile(i[1])[1]])
		#Week day
		sessions_views.rendor(["day", i[2]])
		#Start time
		sessions_views.rendor(["start_time", i[3]])
		#End time
		sessions_views.rendor(["end_time", i[4]])
		#Duration
		sessions_views.rendor(["duration", i[3].split(":"), i[4].split(":")])
		#Category
		sessions_views.rendor(['category', i[8]])
		#Room data
		room_row = room_controller.get_room(i[5])
		#Room name
		sessions_views.rendor(["room", room_row[1]])
	else:
		print(error_displays.no_item)
