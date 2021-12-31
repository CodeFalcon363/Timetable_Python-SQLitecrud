"""
===========================
Remove Item from Users
===========================
This module is responsible for determining what to remove from users,
Currently only course (Students) and module (Staffs) is supported
"""

#Permissions
from build.users.security import permissions as user_permission

#Item table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Shell clobal options [e.g. q/Q for quit]
from build.core import shell_options as shell_choice

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


def start_guess(userid, cmd):
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'rem')

	#Permission
	perm = user_permission.check_permission(userid)

	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return
	print("Removing items from users...")

	#Validate comand arguments
	target = cmd[1]
	item = cmd[2]
	fields = items.item_fields
	if target in fields:
		target_list = fields[target]
	else:
		print(error_displays.no_item)
		return
	if item in fields:
		item_list = fields[item]
	else:
		print(error_displays.no_item)
		return


	if len(cmd) < 5 or len(cmd) > 5:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return
	if not target in ('u') or not item in ('c', 's'):
		shell_displays.invalid_args(cmd[0])
		return

	#Init data
	if item == 'c':
		data_remove = 'course'
	elif item == 's':
		data_remove = 'session'
	else:
		data_remove = False
	target = cmd[3]
	item = cmd[4]
	target_field = target.split()[0]
	item_field = item.split()[0]
	target_data = target.replace(target_field + " ", "")
	item_data = item.replace(item_field + " ", "")
	if target_field in target_list:
		target_field = target_list[target_field]
	else:
		shell_displays.invalid_args(cmd[0])
		return
	if item_field in item_list:
		item_field = item_list[item_field]
	else:
		shell_displays.invalid_args(cmd[0])
		return
	remove_success = "Item removed with success...."
	
	#Check user availability
	print("Checking user availability...")
	user_profile = user_controller.get_profile(target_data)

	if user_profile == False:
		#No user accuont found!
		print(error_displays.no_account)
		return
	user_id = user_profile[0]
	perm = user_permission.check_permission(user_id)

	"""
	Check what to remove and finish the process

	"""
	if data_remove != False:
		if data_remove == "course":
			#Removing courses from students
			#Wether user is student
			if not perm in ('student'):
				#Error!
				print(error_displays.no_account)
				return
			#Check wether course is found!
			print("Checking course availability...")
			user_courses = course_controller.get_courses(target_data, target_field)
			if user_courses == False:
				#No courses found for current user
				print(error_displays.no_item)
				return
			#Remove course
			user_courses = user_courses[0]
			course_id = user_courses[0]
			removed = user_controller.remove_course(user_id, course_id)
			if removed:
				print(remove_success)
				print(target_field + target_data)
				print(item_field + item_data)
	else:
		shell_displays.invalid_args(cmd[0])
		return


