"""
======================
User Data Updating
======================
This module is responsible for updating user profile data
If current user has no preveleges, nothing is processed

"""

#Database
import config

#Permissions
from build.users.security import permissions as user_permission

#User table fields
from build.core.inputs import items

#Error displays
from vendor.views.core import error_prompt as error_displays

#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Password handling
from passlib.hash import bcrypt

#User profile 
from build.core.controllers import users as user_controller


"""

"""
def boot(userid, cmd):
	#Permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'alt')

	#Set password hasher
	hasher = bcrypt.using(rounds=13)  # Make it slower

	#Validate comand arguments
	if len(cmd) < 4:
		#Invalid arguments
		shell_displays.invalid_args(cmd[0])
		return
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return

	#Check scope to search user with

	raw_keyw = cmd[2].split()

	#Validation
	if len(raw_keyw) < 2:
		shell_displays.invalid_args(cmd[0])
		return

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
		return

	#Check wether using email or id
	#If not, return error and force email/id
	if not raw_field in ('ui', 'ue'):
		#Invalid user selection!
		print(error_displays.no_account)
		return


	"""
	=====================
	Update User Profile
	=====================
	At this stage all validations have passed!
	Query database using field as the filed to use and keyw as the string to search user with
	Retrieve user from table using keyw as search using the selected field
	Update profile data and display newly updated user for confirmation

	"""

	#Inform account updating

	print("Updating user using " + keyw + " as user " + field)

	conn = config.con #Establish connection to the database!
	cur = conn.cursor()

	#Check user availability!
	print("Checking user availability...")
	user_row = user_controller.get_profile(keyw)

	#Is user found!???
	if user_row == False:
		print(error_displays.no_account)
		return
	if len(user_row) < 1:
		print(error_displays.no_account)
		return


	#User is found!
	print("User found...")

	#New user profile
	new_profile = {}

	#Create profile data for current user

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

	#End updating new user profile

	#Check wether user account type is being changed
	if 'account' in new_profile:
		#Accoutn is being updated!
		print("Checking account type availability...")
		new_account = new_profile['account']
		if not new_account in user_permission.prevs:
			print(error_displays.invalid_account_type)
			return

	#Check wether password is being updated
	if 'password' in new_profile:
		print("Encrypting new user password...")
		#Password being updated, hash new password before update
		hashed_password = hasher.hash(new_profile['password'])
		new_profile['password'] = hashed_password

	#Start profile data updating
	user_id = user_row[0]

	for i in new_profile:
		#Loop through arguments passed!
		if i != 'id':
			#Not id, update data
			if i != field:
				print("Updating user " + i + "...")
				updated = user_controller.update_user(i, new_profile[i], user_id)
				if updated:
					#Updated!
					print("User " + i + " updated....")

	print("New user profile updated successfully!")







