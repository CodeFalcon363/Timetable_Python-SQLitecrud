"""

"""

_choices = {
#Users arguments
	"-u" : {
		"-ui" : "User ID",
		"-ue" : "User email address",
		"-up" : "User account login password",
		"-un" : "User names",
		"-ua" : "User account type (use staff or student or admin for respective account types)"
	},
#Courses arguments
	"-c" : {
		"-ci" : "Course ID",
		"-cn" : "Course name",
		"-cs" : "Course slug (e.g. web_dev)"
	},
#Modules arguments
	"-m" : {
		"-mi" : "Module ID",
		"-mn" : "Module name",
		"-ms" : "Module slug",
		"-mc" : "Module course"
	},
#Sessions arguments
	"-s" : {
		"-si" : "Session ID",
		"-st" : "Session tutor (can be user id or email address)",
		"-sd" : "Session week day (can be any day between mon-fri",
		"-sb" : "Session begining time (e.g. 10:30)",
		"-se" : "Session end time (e.g. 12:30)",
		"-sr" : "Session room (use room id or room slug)",
		"-ss" : "Session slug (Unique identifier for the session)",
		"-sc" : "Session category (use 1 for On-Campus and 2 for Off-Campus)"

	},
#Rooms arguments
	"-r" : {
		"-ri" : "Room ID",
		"-rn" : "Room name",
		"-rs" : "Room slug (Unique identifier for the room)"
	}
}