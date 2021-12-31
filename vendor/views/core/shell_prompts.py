"""
*****************************************************

********************SHELL PROMPTS MODULE*********************


"""


#Shell display messages
from vendor.views.core import shell_prompts as shell_displays

#Shell windows/items
from build.core.inputs import items as shell_windows

#Shell window/item choices
from vendor.views.docs import choices as shell_choices

#New data creation prompts
from vendor.views.actions.create import prompts as new_create_prompt

#How to quit [./ = q/Q]
quit_option = "Enter q/Q to quit"

#How to cancel action [./ = 0/00]
cancel_option = "Enter 0/00 to cancel"


#Session ended
quit_success = """
******************************
**********[~ QUIT ~]*********
******************************

Did you enter q/Q?
You have just ended this session successfuly!

To restart again
use below comand;

python3 main.py

Bye!
"""

#Process cancelled
cancel_success = """
Successfully cancelled!
"""


"""
Help welcome  [./ = -h]

The function to load the docs is build.core.docs.display_doc()

"""
help_option = """
******************************
**********[~ HELP ~]**********
******************************

User gide/docs
"""

#Comand syntax

_syntax = """
***********
SYNTAX
***********

[COMAND] [-ITEM] [-KEY] [VALUE]
"""

_keys = """
********************
[~ KEY ~]
 Type -h [ITEM] to see available options 
"""


"""
================
Invalid Comand
================

"""
def invalid_comand(cmd):
	print("*" * 35)
	print("[~ INVALID COMAND ~]: " + str(cmd) + "")
	print("*" * 35)
	print(_syntax)
	print("Type -h for help")

#Session ended
quit_success = """
******************************
**********[~ QUIT ~]*********
******************************

Did you enter q/Q?
You have just ended this session successfuly!

To restart again
use below comand;

python3 main.py

Bye!
"""


"""


"""

def _items():
	
	#Print available items
	items_list = shell_windows._items
	print("""
********************
[~ ITEMS ~]
Available items are;
		""")
	for j in items_list:
		print(str(j) + ":\t" + str(items_list[j]))


"""


"""

def _choices(cmd):
	
	#Print available items
	items_list = shell_choices._choices
	print("""********************
[~ KEY ~]
Available options for this comand are;
		""")
	if cmd in items_list:
		j = items_list[cmd]
		
		#Display docs
		for i in j:
			print(str(i) + "\t:" + str(j[i]))


"""

"""
def cmd_user(perm):
	return "[~ " + str(perm) + " ~]: "


"""

"""
def add_data(data, item):
	print("*" * 30)
	print("Creating new " + str(item) + "")
	print("*" * 30)
	promt_list = new_create_prompt.prompt[item]
	data_prompt = promt_list[data]
	print("[~ create ~]: [~ " + str(item) + " ~]: " + str(data_prompt) + "\n")


"""

"""
def invalid_args(cmd):
	print("*" * 30)
	print("[~ " + str(cmd) + " ~]: Invalid/few arguments passed!")
	print("*" * 30)


"""
Confirm user action
"""

def confirm_action(action = False):
	if action:
		print("""
***********************
CONFIRMATION REQUIRED!
***********************
""")
	else:
		print("Enter y/Y to confirm\nEnter any key to cancel")
