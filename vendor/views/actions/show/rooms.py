"""
======================
Rooms View
======================

When showing room data,
we will use this view to render the data

@param room_data{} => module data
"""

#Error displays
from vendor.views.core import error_prompt as error_displays

#Modules configs
from configs import modules as module_configs


"""

"""

def rendor(room_data):

	#Display room name
	if room_data[0] == "name":
		print("""Room:				          """ + room_data[1])
		return

	#Display room slug
	if room_data[0] == "slug":
		print("""Slug:				   """ + room_data[1])
		return

	#Display room profile name
	if room_data[0] == "profile_name":
		print("*" * 50)
		print("""Room:				          """ + room_data[1])
		print("*" * 50)
		return