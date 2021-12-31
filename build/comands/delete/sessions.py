"""
======================
Session Deletion
======================
This module is responsible for deleting sessions
If current user has no preveleges, nothing is processed

"""

#Permissions
from build.users.security import permissions as user_permission

#Room table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

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


"""

"""
def boot(userid, cmd):
	#Permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'del')

	#Permission
	perm = user_permission.check_permission(userid)

	#Validate comand arguments
	if len(cmd) < 3:
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
	Delete Session Data
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search session with
	Retrieve session from table using keyw as search using the selected field
	Delete session data and return success message

	"""

	print("Deleting session using " + keyw + " as room " + field)

	#Check item availability!
	print("Checking session availability...")
	item_row = session_controller.search_session(keyw, field)

	#Is course found!???
	if item_row == False:
		print(error_displays.no_item)
		return


	#Course is found!
	item_id = item_row[0][0]

	#Confirm course deletion

	shell_displays.confirm_action()
	shell_displays.confirm_action(True)
	print("The session with [" + field + "] " + keyw + " will be deleted")
	is_confirm = input(shell_displays.cmd_user(perm))
	if is_confirm in ('y', 'Y'):
		#User just confirmed room deletion
		#Delete room

		deleted = session_controller.delete_session(item_id)
		if deleted:
			#Session deleted!
			print("Session deleted successfully!")
	else:
		print("Cancelled!")







