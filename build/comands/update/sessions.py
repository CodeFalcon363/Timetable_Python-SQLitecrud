"""
======================
Session Data Updating
======================
This module is responsible for updating session profile data
If current user has no preveleges, nothing is processed

"""

#Permissions
from build.users.security import permissions as module_permission

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


"""

"""
def boot(moduleid, cmd):
	#Permissions
	allow = module_permission.allowed(module_permission.check_permission(moduleid), 'alt')

	#Validate comand arguments
	if len(cmd) < 4:
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
	=====================
	Update Session Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search session with
	Retrieve session from table using keyw as search using the selected field
	Update profile data and display newly updated session for confirmation

	"""

	print("Updating session using " + keyw + " as session " + field)

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
	print("Checking session availability...")
	item_rows = session_controller.get_session(keyw)

	#Is item found!???
	if item_rows == False:
		print(error_displays.no_item)
		return
	#Must be found!
	print("Session profile found...")
	#Room availability!
	if 'room' in new_profile:
		print("Checking room availability...")
		#Update room with id
		room_id = room_controller.get_room(new_profile['room'])
		if room_id == False:
			#No room found!
			print(error_displays.no_item)
			return
		#Update with id
		print("Room profile found...")
		new_profile['room'] = room_id[0]

	#Tutor availability!
	if 'tutor' in new_profile:
		print("Checking tutor availability...")
		#Update tutor with id
		tutor_id = user_controller.get_profile(new_profile['tutor'])
		if tutor_id == False:
			#No data found!
			print(error_displays.no_item)
			return
		#Update with id
		print("Tutor found...")
		new_profile['tutor'] = tutor_id[0]

	#Module availability!
	if 'module' in new_profile:
		print("Checking module availability...")
		#Update module with id
		module_id = module_controller.guess_modules(new_profile['module'])
		if module_id == False:
			#No data found!
			print(error_displays.no_item)
			return
		#Update with id
		print("Module profile found...")
		new_profile['module'] = module_id[0][0]

	#Week-days confirm
	if 'day' in new_profile:
		#Confirm the selected day exists!
		if not new_profile['day'] in items.week_days:
			print(error_displays.no_item)
			return
		#End confirmation

	#Check slug availability!
	if 'slug' in new_profile:
		#Slug being updated

		if field != 'slug':
			#Field not slug
			print("Checking session slug availability...")
			item_row = session_controller.search_session(new_profile['slug'], 'slug')

			if item_row != False:
				#Name taken
				print(error_displays.no_name)
				return

	#All is well, update data
	item_id = item_rows[0]

	for i in new_profile:
		#Loop through arguments passed!
		if i != 'id':
			#Not id, update data
			if i != field:
				print("Updating session " + i + "...")
				updated = session_controller.update_session(i, new_profile[i], item_id)
				if updated:
					#Updated!
					print("Session " + i + " updated....")

	print("New session profile updated with success")







