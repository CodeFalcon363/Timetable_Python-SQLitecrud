"""
======================
Module Deletion
======================
This module is responsible for deleting course modules
If current user has no preveleges, nothing is processed

"""

#Database
import config

#Permissions
from build.users.security import permissions as user_permission

#Room table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays


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
	Delete Module Data
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search module with
	Retrieve module from table using keyw as search using the selected field
	Delete module data and return success message

	"""

	print("Deleting module using " + keyw + " as module " + field)

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Check item availability!

	sql = "SELECT id FROM modules WHERE " + field + "=?"

	cur.execute(sql, [keyw])

	item_row = cur.fetchall()

	#Is course found!???
	if len(item_row) < 1:
		print(error_displays.no_item)
		return


	#Course is found!
	item_id = item_row[0][0]

	#Confirm course deletion

	shell_displays.confirm_action()
	shell_displays.confirm_action(True)
	print("The module with [" + field + "] " + keyw + " will be deleted")
	is_confirm = input(shell_displays.cmd_user(perm))

	if is_confirm in ('y', 'Y'):
		#User just confirmed module deletion
		#Delete module

		sql = "DELETE FROM modules WHERE " + field + "=?"
		cur.execute(sql, [keyw])
		conn.commit()
		#Room deleted!

		print("Module deleted successfully!")
	else:
		print("Cancelled!")







