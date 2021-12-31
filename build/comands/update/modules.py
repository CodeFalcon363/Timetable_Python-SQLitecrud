"""
======================
Module Data Updating
======================
This module is responsible for updating module profile data
If current module has no preveleges, nothing is processed

"""

#Permissions
from build.users.security import permissions as user_permission

#Module table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#User profile 
from build.core.controllers import users as user_controller

#Course profile
from build.core.controllers import courses as course_controller

#Modules profile
from build.core.controllers import modules as module_controller



"""

"""
def boot(userid, cmd):
	#Permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'alt')

	#Permission
	perm = user_permission.check_permission(userid)

	#Validate comand arguments
	if len(cmd) < 4:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return 1
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Check scope to search module with

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
	Update Module Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search module with
	Retrieve module from table using keyw as search using the selected field
	Update profile data and display newly updated module for confirmation

	"""

	print("Updating module using " + keyw + " as module " + field)

	#New item profile
	new_profile = {}

	#Create profile data for current item

	filed_lists = items.item_fields[cmd[1]]

	for i in cmd:
		#Loop through all currently selected arguments
		j = i.split()
		if len(j) > 1:
			#Thats an argument!
			raw_field = j[0]

			#Update new user profile
			if raw_field in filed_lists:
				key_value = i.replace(raw_field + " ", "")
				new_profile[filed_lists[raw_field]] = key_value

	#End updating new item profile

	#Update user with id
	if 'tutor' in new_profile:
		#Updating module tutor!
		print("Checking staff availability...")
		tutor_guess = new_profile['tutor']
		tutor_row = user_controller.get_profile(tutor_guess)
		#Is user found!
		if tutor_row == False:
			#No tutor found!
			print(error_displays.no_account)
			return

		if len(tutor_row) < 1:
			#No tutor found!
			print(error_displays.no_account)
			return
		#Update with id
		print("Staff account found...")
		new_profile['tutor'] = tutor_row[0]

	#Update course with course id
	if 'course' in new_profile:
		print("Checking course availability...")
		#Updating course
		course_guess = new_profile['course']
		course_row = course_controller.get_courses(course_guess)
		#Is course found?
		if course_row == False:
			#No course found!
			print(error_displays.no_item)
			return

		if len(course_row) < 1:
			#No course found!
			print(error_displays.no_item)
			return
		#Update with id
		print("Course found...")
		new_profile['course'] = course_row[0][0]

	#Item availability!
	print("Checking module availability...")
	item_rows = module_controller.get_modules(keyw, field)

	#Is module found!???
	if item_rows == False:
		print(error_displays.no_item)
		return

	if len(item_rows) < 1:
		print(error_displays.no_item)
		return
	print("Module found...")
	#Check name availability!
	if 'name' in new_profile:
		#Name being updated
		print("Checking module name availability...")
		item_row = module_controller.get_modules(new_profile['name'], 'name')
		#Is found?
		if item_row != False:
			#Name taken
			print(error_displays.no_name)
			return

	#Check slug availability!
	if 'slug' in new_profile:
		#Slug being updated
		if field != 'slug':
			#Field not slug
			print("Checking module slug availability...")
			item_row = module_controller.get_modules(new_profile['slug'], 'slug')

			#Is found?
			if item_row != False:
				#Name taken
				print(error_displays.no_name)
				return

	#All is well, update data
	item_id = item_rows[0][0]

	for i in new_profile:
		#Loop through arguments passed!
		if i != 'id':
			#Not id, update data
			if i != field:
				print("Updating module " + i + "...")
				updated = module_controller.update_module(i, new_profile[i], item_id)
				if updated:
					#Updated!
					print("Module " + i + " updated....")

	print("New module profile updated with success")







