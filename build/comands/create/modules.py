"""
======================
New Module Creating
======================
This module is responsible for creating new course modules records
If current user has no preveleges, nothing is processed

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

#Modules profile
from build.core.controllers import modules as module_controller

#Courses profile
from build.core.controllers import courses as course_controller

#Display module data views
from vendor.views.actions.show import modules as modules_views


"""

"""
def boot(userid, cmd):

	#New module profile
	new_profile = {}
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'new')
	#Permission
	perm = user_permission.check_permission(userid)
	
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Create profile data for new module

	filed_lists = items.item_fields[cmd[1]]

	for i in cmd:
		#Loop through all currently selected arguments
		j = i.split()
		if len(j) > 1:
			#Thats an argument!
			raw_field = j[0]

			#Update new module profile
			if raw_field in filed_lists:
				key_value = i.replace(raw_field + " ", "")
				new_profile[filed_lists[raw_field]] = key_value

	#End updating new module pforile

	#Validation of new module profile completion

	for i in filed_lists:
		#Check wether its id
		if filed_lists[i] != 'id':
			#Not id, check wether it has been set for our new module
			if not filed_lists[i] in new_profile:
				#Not updated, force selection
				shell_displays.add_data(filed_lists[i], "module")
				print(shell_displays.quit_option)
				print(shell_displays.cancel_option)
				cmd = input(shell_displays.cmd_user(perm))
				shell_choice.is_quit(cmd)
				shell_choice.is_cancel(userid, cmd)
				new_profile[filed_lists[i]] = cmd

	#End updating new module profile

	"""
	=====================
	Creating Module Profile
	=====================
	At this stage all validations have passed!
	Query database to see if slug is available, if available save new module profile
	After creating display newly created module to confirm

	"""

	print("Creating new module as " + new_profile['name'])
	#Name availability
	print("Checking name availability for " + new_profile['name'] + "...")
	item_row = module_controller.get_modules(new_profile['name'], "name")

	#If name available
	if item_row == False:
		print("Name available as " + new_profile['name'] + "...")
	elif len(item_row) > 0:
		#Name taken
		print(error_displays.no_name)
		return

	#Check slug availability!
	print("Checking slug availability for " + new_profile['slug'] + "...")
	item_row = module_controller.get_modules(new_profile['slug'], "slug")

	if item_row == False:
		print("Slug available as " + new_profile['slug'] + "...")
	elif len(item_row) > 0:
		#Slug taken
		print(error_displays.no_name)
		return

	#All is well, create new item

	#Update course with course id
	course_guess = new_profile['course']
	print("Searching for course as " + str(course_guess))
	course_row = module_controller.get_course(course_guess)

	#Have we got any result
	if course_row == False:
		#No course
		print(error_displays.no_item)
		return

	if len(course_row) < 1:
		#No course found!
		print(error_displays.no_item)
		return
	#Update with id
	print("Found course as " + str(course_row[0][1]))

	new_profile['course'] = course_row[0][0]

	module_saved = module_controller.save_module([new_profile['name'], 
		new_profile['slug'],
		new_profile['course']])

	#Inform created
	if module_saved:
		print("New module created with success")

	#Display newly created module data
	modules_views.rendor(['profile_name', new_profile['name']])







