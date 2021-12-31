"""
======================
Room Data Updating
======================
This module is responsible for updating room profile data
If current module has no preveleges, nothing is processed

"""

#Permissions
from build.users.security import permissions as module_permission

#Module table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Rooms profile
from build.core.controllers import rooms as room_controller


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

	#Check scope to search room with

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
	Update Room Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search room with
	Retrieve room from table using keyw as search using the selected field
	Update profile data and display newly updated room for confirmation

	"""

	print("Updating room using " + keyw + " as room " + field)

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
	print("Checking room availability...")
	item_rows = room_controller.get_room(keyw)

	#Is item found!???
	if item_rows == False:
		print(error_displays.no_item)
		return

	#Check name availability!
	if 'name' in new_profile:
		#Name being updated
		print("Checking room name availability...")
		item_row = room_controller.search_room(new_profile['name'], 'name')

		if item_row != False:
			#Name taken
			print(error_displays.no_name)
			return

	#Check slug availability!
	if 'slug' in new_profile:
		#Slug being updated

		if field != 'slug':
			#Field not slug
			print("Checking room slug availability...")
			item_row = room_controller.search_room(new_profile['slug'], 'slug')

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
				print("Updating room " + i + "...")
				updated = room_controller.update_room(i, new_profile[i], item_id)
				if updated:
					#Updated!
					print("Room " + i + " updated....")

	print("New room profile updated with success")







