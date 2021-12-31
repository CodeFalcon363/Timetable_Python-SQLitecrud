"""
======================
Docs Module
======================
This module is used to display user docs/guides to users
Every guide/doc displayed by the comand [-h] or [-h [-item]] is here.
Divided into two parts;
all_docs{}
Holds docs about evey comand

item_docs{}
Holds docs about every item

"""

all_docs = {
#Show comands
"show": """
*****************
 [~ show ~]
*****************

 Use this comand to display list of data

 [~ USAGE ~]
 show [item] [-key] [value]


 """,
#Create comand

"create": """
****************
 [~ create ~]
****************

 Use this comand to create a new data

 [~ USAGE ~]
 create [item] [-key] [value]

""",

#Update comand

"update": """
*****************
 [~ update ~]
*****************

 Use this comand to update data

 [~ USAGE ~]
 update [item] [-key] [value]

 *****
 NOTE:
 *****
 The first argument will be used as the item to update 
 and the rest arguments are used to update the old data 
 with the values passed

 [e.g.]
 update -u -ue example@mail.domain -un John Doe
 This will update names for user with email example@mail.domain to John Doe

 """,
#Delete comand

 "delete": """
****************
 [~ delete ~]
****************

 Use this comand to delete data

 [~ USAGE ~]
 delete [item] [-key] [value]

 *****
 NOTE:
 *****
 The comand accepts only one argument

 [e.g.]
 delete -u -ui 2

 Will delete user with id 3

""",
#Assign comand

 "assign": """
****************
 [~ assign ~]
****************

 Use this comand to assign item to an item

 [~ USAGE ~]
 assign [assigning_item] [item_to_assign] [-key] [value]

 *****
 NOTE:
 *****
 The comand can work on users only!

 [e.g: 1.]
 assign -u -c -ui 2 -ci 1

 Will assign course with id 1 to user with id 2
 The user must be a student

  [e.g: 2.]
 assign -u -m -ui 2 -mi 1

 Will assign module with id 1 to user with id 2
 The user must be a staff

""",
#Remove comand

 "remove": """
****************
 [~ remove ~]
****************

 Use this comand to remove previously assigned item from an item

 [~ USAGE ~]
 remove [item_to_remove_from] [item_to_remove] [-key] [value]

 *****
 NOTE:
 *****
 The comand works on users only!

 [e.g: 1.]
 remove -u -c -ui 2 -ci 1

 Will remove course with id 1 from list of courses assigned to user with id 2
 The user must be a student

  [e.g: 1.]
 remove -u -s -ui 2 -si 1

 Will remove session with id 1 from list of sessions assigned to user with id 2
 The user must be a staff
""",
#Report comand

 "report": """
****************
 [~ report ~]
****************

 Use this comand to display an overview report of data

 [~ USAGE ~]
 report [item] [-key] [value]

 [e.g.]
 report -u -ui 2

 Will display overview report for user with id 3
"""

 }


"""
======================
Items Documentations
======================
This is used to display documentations for each choice available under a comand

 """

item_docs = {
#User item
"-u" : """
****************
 [~ -u ~]
****************

 This item referes to users

 [~ USAGE ~]
 [comand] [-u] [-key] [value]

 ******
 NOTE:
 ******
 When creating new user accounts, use below options as account type;
 [staff]
 Staffs accounts
 [student]
 Students accounts
 [admin]
 Admins accounts

 [e.g.]
 delete -u -ui 2

 Will delete user with id 3
""",

#Course item
"-c" : """
****************
 [~ -c ~]
****************

 This item referes to courses

 [~ USAGE ~]
 [comand] [-c] [-key] [value]


 [e.g.]
 delete -c -ci 2

 Will delete course with id 3
 and also delete all modules under the course!
""",

#Module item
"-m" : """
****************
 [~ -m ~]
****************

 This item referes to course modules

 [~ USAGE ~]
 [comand] [-m] [-key] [value]


 [e.g.]
 delete -m -mi 2

 Will delete module with id 3
 To update or assign a module to another course,
 use the update comand and set the module course to a defferent course

 [e.g: 1]

 update -m -mi 2 -mc web-dev
 Above comand will update module with id 2 and set
  it's course to the course with slug web-dev
""",

#Sessions item
"-s" : """
****************
 [~ -s ~]
****************

 This item referes to module sessions

 [~ USAGE ~]
 [comand] [-s] [-key] [value]


 [e.g.]
 delete -s -si 2

 Will delete session with id 3
 Sessions are course modules which are assigned to staffs
 Each course module can have as many sessions as required
 weekly (mon-fri)

 [e.g: 1]

 update -s -si 2 -sm front-end
 Above comand will update session with id 2 and set
  it's module to the module with slug front-end
""",

#Rooms item
"-r" : """
****************
 [~ -r ~]
****************

 This item referes to rooms

 [~ USAGE ~]
 [comand] [-r] [-key] [value]


 [e.g.]
 delete -r -ri 2

 Will delete room with id 3
 Remember to update sessions that depend on this room with
 new or available room

 [e.g: 1]

 update -r -ri 2 -rn Web Developers Class
 Above comand will update room with id 2 and set
  it's name to Web Developers Class
"""

 }


