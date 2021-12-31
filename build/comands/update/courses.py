"""
======================
Course Data Updating
======================
This module is responsible for updating course data
If current module has no preveleges, nothing is processed

"""

#Database
import config

#Permissions
from build.users.security import permissions as module_permission

#Module table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Course profile
from build.core.controllers import courses as course_controller


"""

"""
def boot(moduleid, cmd):
	#Permissions
	allow = module_permission.allowed(module_permission.check_permission(moduleid), 'alt')

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Validate comand arguments
	if len(cmd) < 4:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return 1
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Check scope to search course with

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
	Update Course Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search course with
	Retrieve course from table using keyw as search using the selected field
	Update profile data and display newly updated course for confirmation

	"""

	print("Updating course using " + keyw + " as course " + field)

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

	#Item availability!
	print("Checking course availability...")
	item_rows = course_controller.get_courses(keyw, field)

	#Is course found!???
	if item_rows == False:
		print(error_displays.no_item)
		return

	if len(item_rows) < 1:
		print(error_displays.no_item)
		return

	#Course is found!
	print("Course found...")

	#Check name availability!
	if 'name' in new_profile:
		#Name being updated
		print("Checking course name availability...")
		item_row = course_controller.get_courses(new_profile['name'], 'name')

		if item_row != False:
			#Name taken
			print(error_displays.no_name)
			return

	#Check slug availability!
	if 'slug' in new_profile:
		#Slug being updated

		if field != 'slug':
			#Field not slug
			print("Checking course slug availability...")
			item_row = course_controller.get_courses(new_profile['slug'], 'slug')

			if litem_row != False:
				#Slug taken
				print(error_displays.no_slug)
				return

	#All is well, update data
	item_id = item_rows[0][0]

	for i in new_profile:
		#Loop through arguments passed!
		if i != 'id':
			#Not id, update data
			if i != field:
				print("Updating course " + i + "...")
				updated = course_controller.update_course(i, new_profile[i], item_id)
				if updated:
					#Updated!
					print("Course " + i + " updated....")

	print("New course profile updated with success")







