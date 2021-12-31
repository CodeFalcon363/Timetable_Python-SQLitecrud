"""
===================
Sessions Views
===================


"""

#Item table fields

from build.core.inputs import items

#Handle sessions duration
import datetime

def rendor(session_data):
	#Display session profile

	#Print session week day
	if session_data[0] == "day":
		print("""Day:			                     """ + str(items.week_days[session_data[1]]))
		return

	#Print session start time
	if session_data[0] == "start_time":
		print("""Start Time:			     """ + str(session_data[1]))
		return

	#Print session end time
	if session_data[0] == "end_time":
		print("""End Time:			     """ + str(session_data[1]))
		return


	#Print session duration
	if session_data[0] == "duration":
		start = int(session_data[1][0]) + (int(session_data[1][1])/60)
		end = int(session_data[2][0]) + (int(session_data[2][1])/60)
		if end < start:
			end = end + 12
		duration = (end - start)
		print("""Duration:			       """ + str(datetime.timedelta(hours=duration)).rsplit(":", 1)[0] + " hrs")
		return


	#Print session room
	if session_data[0] == "room":
		print("""Room:			                 """ + str(session_data[1]))
		return

	#Print session tutor
	if session_data[0] == "tutor":
		print("""Tutor:			                    """ + str(session_data[1]))
		return

	#Print session tutor workload
	if session_data[0] == "work_load":
		print("""Workload:			     """ + str(session_data[1]) + """% """)
		return

	#Print session tutor sessions count
	if session_data[0] == "tutor_sessions":
		print("""Total Sessions:			 """ + str(session_data[1]))
		return

	#Sessions tutor hours (weekly)
	if session_data[0] == "tutor_hours":
		print("""Total Hours:			    """ + str(session_data[1]) + """ hrs""")
		return

	#Print session category
	if session_data[0] == "category":
		category_list = items.event_category
		guess_event = session_data[1]
		if guess_event in category_list:
			guess_event = category_list[guess_event]
		else:
			guess_event = "Unknown"
		print("""Event Category:		      """ + str(guess_event))
		return
		

