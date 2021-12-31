"""
===========================
User Report Module
===========================
This module is responsible for display overview report for users
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

#When displaying user profile data
#We will use views from this folder/package
from vendor.views.actions.show import users as user_show

#Course profile
from vendor.views.actions.show import courses as course_views

#Course profile
from vendor.views.actions.show import sessions as session_views

#Handle sessions duration
import datetime



"""

"""

def start_guess(userid, cmd):
	#Current action permissions
	allow = user_permission.allowed(user_permission.check_permission(userid), 'rep')

	#Permission
	perm = user_permission.check_permission(userid)
	#Confirm allow
	if not allow:
		print(error_displays.access_denied)
		return
	#Comand validation
	if len(cmd) < 3:
		shell_displays.invalid_args(cmd[0])
		return
	#Arguments validation
	user_args = items.item_fields['u']
	user_field = cmd[2].split()[0]
	user_data = cmd[2].replace(user_field + " ", "")
	if not cmd[1] in ('u') or not user_field in user_args:
		shell_displays.invalid_args(cmd[0])
		return
	user_field = user_args[user_field]

	print("Loading report data for user with " + str(user_field) + " " + str(user_data))

	#User availability...
	print("Checking user availability...")
	user_profile = user_controller.get_profile(user_data)
	if user_profile == False:
		#Nothing found!
		print(error_displays.no_account)
		return

	#User accout found!
	new_profile = {}
	new_profile['name'] = user_profile[1]
	new_profile['email'] = user_profile[2]
	new_profile['account'] = user_permission.check_permission(user_profile[0])
	user_show.rendor(new_profile)
	
	#Now load users general report
	"""
	We load courses, and off/on campus sessions for students,
	We load workload (%) for staffs and show their current usage
	We assume that assigning lessons are on weekly basis, 
	so the calculation for Monday is assumed to affect all mondays in the whole semester

	"""

	#Data used for calculations
	#@Init
	on_campus = 0
	off_campus = 0
	hours = 0

	#Load courses for students
	if user_permission.check_permission(user_profile[0]) == "student":
		#This user is a student, we load each course along with off/oncapmus
		#sessions and their percentage
		user_courses = user_controller.get_courses(user_profile[0]) #Use user id to fetch courses
		if user_courses == False:
			#No courses assigned for this user!
			print(error_displays.no_course)
			return

		#Load courses
		for i in user_courses:
			#Display course profile name
			print("\n")
			course_views.rendor(course_controller.get_courses(i[0])[0][1])
			#Load modules for this course
			course_modules = course_controller.get_modules(i[0])
			#Does this course have any modules
			if course_modules == False:
				print(error_displays.no_module)
			else:
				#Display total modules found for the course
				course_views.profile(["modules", len(course_modules)])
				#Loop through the modules to load sessions
				for i in course_modules:
					#Load sessions data
					module_sessions = session_controller.module_sessions(i[0]) #Use id to load sessions for each module
					#Does this module have any sessions!
					if module_sessions == False:
						#No sessions found for this module
						pass
					else:
						#Something has been found!
						for i in module_sessions:
							#Loop through all the module sessions
							#Is this session off campus or on campus?
							if i[8] == "1":
								#Thats on campus
								on_campus = on_campus + 1
							else:
								#Thats off campus
								off_campus = off_campus + 1
				#Display course session categories
				total_sessions = int((on_campus + off_campus))
				on_campus_percentage = (int(on_campus)/int(total_sessions)) * 100
				off_campus_percentage = (int(off_campus)/int(total_sessions)) * 100
				course_views.profile(["on_campus", on_campus, on_campus_percentage])
				course_views.profile(["off_campus", off_campus, off_campus_percentage])
		#END Loading data for students
		return

	#Load workload for staffs
	if user_permission.check_permission(user_profile[0]) == "staff":
		#Load sessions and workload
		sessions_count = 0
		user_sessions = user_controller.get_sessions(user_profile[0]) #Use id to fetch sessions
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
				hours = hours + duration
				sessions_count = sessions_count + 1
		raw_hours = str(datetime.timedelta(hours=hours)).rsplit(":", 1)[0]
		hours = int((hours/18) * 100)
		#Render total sessions by staff
		session_views.rendor(["tutor_sessions", sessions_count])
		#Render total hours (weekly)
		session_views.rendor(["tutor_hours", raw_hours])
		#Render total workload for tutor
		session_views.rendor(["work_load", hours])
		print("\n")

		#END displaying report for staff accounts
		return




