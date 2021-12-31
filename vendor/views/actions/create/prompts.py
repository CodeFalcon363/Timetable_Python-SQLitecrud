"""

"""

prompt = {
	"user" : {
		"name" : "Enter User Names",
		"email" : "Enter User Email address",
		"password" : "Enter User Password",
		"account" : "Select Account type  [ -h -u for help ]"
	},

	"course" : {
		"name" : "Enter Course Name",
		"slug" : "Enter Course Slug"
	},

	"module" : {
		"name" : "Enter Module Name",
		"slug" : "Enter Module Slug",
		"course" : "Enter Module Course [ course slug or id ]"
	},

	"sessions" : {
		"slug" : "Enter Session Slug",
		"module" : "Enter Session Module [ module slug or id ]",
		"room" : "Enter Session Room [ room slug or id ]",
		"tutor" : "Session Tutor [staff id or email]",
		"start" : "Session Start Time [e.g. 10:00]",
		"end" : "Session Finish Time [e.g. 12:00]",
		"day" : "Session Week Day [e.g. mon]",
		"cat" : "Session category [use 1 for on-campus or 2 for off-campus]"
	},

	"room" : {
		"name" : "Enter Room Name",
		"slug" : "Enter Room Slug"
	}
}