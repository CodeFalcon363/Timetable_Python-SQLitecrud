"""
======================
New Sessions Creating
======================
This file is responsible for creating new sessions records
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

#To get room id
from build.core.controllers import rooms as room_controller

#Sessions controller file
from build.core.controllers import sessions as session_controller

#User profile and id
from build.core.controllers import users as user_controller

#Module profile and id
from build.core.controllers import modules as module_controller


"""

"""
def boot(userid, cmd):

	#New item profile
	new_profile = {}
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'new')
	#Permission
	perm = user_permission.check_permission(userid)
	
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return 1

	#Create profile data for new sessions

	filed_lists = items.item_fields[cmd[1]]

	for i in cmd:
		#Loop through all currently selected arguments
		j = i.split()
		if len(j) > 1:
			#Thats an argument!
			raw_field = j[0]

			#Update new room profile
			if raw_field in filed_lists:
				key_value = i.replace(raw_field + " ", "")
				new_profile[filed_lists[raw_field]] = key_value

	#End updating new session profile

	#Validation of new session profile completion

	for i in filed_lists:
		#Check wether its id
		if filed_lists[i] != 'id':
			#Not id, check wether it has been set for our new session
			if not filed_lists[i] in new_profile:
				#Not updated, force selection
				shell_displays.add_data(filed_lists[i], "sessions")
				print(shell_displays.quit_option)
				print(shell_displays.cancel_option)
				cmd = input(shell_displays.cmd_user(perm))
				shell_choice.is_quit(cmd)
				shell_choice.is_cancel(userid, cmd)
				new_profile[filed_lists[i]] = cmd

	#End updating new session profile

	"""
	=====================
	Creating Session Profile
	=====================
	At this stage all validations have passed!
	Query database to see if slug is available, if available save new item profile
	After creating display newly created session to confirm

	"""

	print("Creating new session...")
	
	#Check slug availability

	if session_controller.get_session(new_profile['slug']) != False:
		#Slug taken
		print(error_displays.no_slug)
		return

	#All is well, create new item

	#Update room with id
	print("Checking room availability...")
	room_id = room_controller.get_room(new_profile['room'])
	if room_id == False:
		#No room found!
		print(error_displays.no_item)
		return
	#Update with id
	new_profile['room'] = room_id[0]

	#Update tutor with id
	print("Checking user availability...")
	tutor_id = user_controller.get_profile(new_profile['tutor'])
	if tutor_id == False:
		#No data found!
		print(error_displays.no_item)
		return
	#Update with id
	new_profile['tutor'] = tutor_id[0]

	#Update module with id
	print("Checking module availability...")
	module_id = module_controller.guess_modules(new_profile['module'])
	if module_id == False:
		#No data found!
		print(error_displays.no_item)
		return
	#Update with id
	new_profile['module'] = module_id[0][0]

	#Confirm the selected day exists!
	print("Confirming selected day...")
	if not new_profile['day'] in items.week_days:
		print(error_displays.no_item)
		return
	#End confirmation

	#Confirm the user has enough workloads left
	#Max teaching hours is 18 hours per staff!
	hours = 0
	sessions_count = 0
	user_sessions = user_controller.get_sessions(tutor_id[0]) #Use id to fetch sessions
	#Do we have anything!
	if user_sessions == False:
		#No sessions found for this user
		pass
	else:
		#Found some sessions
		for i in user_sessions:
			#Loop through all sessions
			#Calculate hours spent on each sessions,
			#Add them and determine the workload for the staff!
			start = i[3].split(":")
			end = i[4].split(":")
			start_time = int(start[0]) + (int(start[1])/60)
			end_time = int(end[0]) + (int(end[1])/60)
			if end_time < start_time:
				end_time = end_time + 12
			duration = (end_time - start_time)
			hours = int(hours + duration)
	#Workload
	new_start = new_profile['start'].split(":")
	new_end = new_profile['end'].split(":")
	new_start_time = int(new_start[0]) + (int(new_start[1])/60)
	new_end_time = int(new_end[0]) + (int(new_end[1])/60)
	if new_end_time < new_start_time:
		new_end_time = new_end_time + 12
	new_hours = new_end_time - new_start_time
	hours = int(hours + new_hours)

	if hours >= 18:
		print(error_displays.no_workload)
		return

	item_saved = session_controller.save_session([new_profile['tutor'], 
		new_profile['day'], 
		new_profile['start'], 
		new_profile['end'],
		new_profile['room'],
		new_profile['module'],
		new_profile['slug'],
		new_profile['cat']])

	#Inform created
	if item_saved == True:
		print("New session created with success")
	else:
		print(item_saved)

	#Display newly created module data
	#print(new_profile)







