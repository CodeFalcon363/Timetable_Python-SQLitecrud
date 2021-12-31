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

#Course profile
from build.core.controllers import courses as course_controller

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

#Course profile
from vendor.views.actions.show import courses as course_views


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

	print("Searching for " + field + " as " + keyw + " in courses...")

	#Try searching for course

	course_row = course_controller.get_courses(keyw, field)

	#Did we find any?
	if course_row != False and len(course_row) > 0:
		#We've got something back
		for i in course_row:
			#Loop through all rows

			#Display course name
			course_views.rendor(i[1])
			modules_row = course_controller.get_modules(i[0])
			#Did we find any modules for this course?
			if modules_row != False and len(modules_row)>0:
				for i in modules_row:
					#Loop through all modules list
					print("\n")
					#Print sesion profile data!
					modules_views.rendor(['name', i[1]])
					#Slug
					modules_views.rendor(['slug', i[2]])
					
				print("\nFinished with " + str(len(modules_row)) + " modlues...")
			else:
				print(error_displays.no_module)


	else:
		print(error_displays.no_item)
		return







