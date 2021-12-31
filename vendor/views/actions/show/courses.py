"""
======================
User Profile View
======================


"""

def rendor(course):
	#Display user profile
	print("-" * 50)
	print("""Course:                                  """ + str(course))

	#Last line to indicate user profile display end!
	print("-" * 50)

#Display course profile
def profile(data):
	#What to display
	#Course modules
	if data[0] == "modules":
		#Displaying course modules count
		print("""Total Modules:                  """ + str(data[1]))
		return

	#Course off campus sessions
	if data[0] == "off_campus":
		#Displaying course modules count
		print("""Off Campus:                       """ + str(data[1]) + """ sessions [ """ + str(data[2]).split(".")[0] + """% ]""")
		return

	#Course on campus sessions
	if data[0] == "on_campus":
		#Displaying course modules count
		print("""On Campus:                       """ + str(data[1]) + """ sessions [ """ + str(data[2]).split(".")[0] + """% ]""")
		return