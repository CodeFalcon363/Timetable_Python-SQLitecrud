"""
*****************************************************

********************ERROR PROMPTS MODULE*********************


@param email > user login email
@param password > user login password 
"""


#No enough previeleges for current user
access_denied = "Access denied!"


#Account login disbaled for current user
login_denied = "You cannot login to that account at this time!"

#When creating new users, if the email has already been registered,
#We will render this view

email_registered = """
***************
 EMAIL TAKEN!
***************

That email has already been registered
Please try again using another email address
You can also reset user password if the user is locked out of their account

use -h update
to learn how to update user login passwords
"""


#When performing actions on user accounts,
#If no user is found matching the search creteria used
#We will render this view

no_account = """
*******************
 NO ACCOUNT FOUND!
*******************

No user account was found matching
Please try again with the correct credentials
Recomended to use email or id to select users
"""

#When performing actions on items,
#If no item is found matching the search creteria used
#We will render this view

no_item = """
*******************
 NO ITEM FOUND!
*******************

No item was found matching
Please try again with the correct credentials
Recomended to use id or slug when selecting items
"""

#When creating new sessions,
#If the selected staff has run out of wrokload limit
#We will render this view

no_workload = """
*******************
 NO MORE WORKLOAD
*******************

The staff you selected has reached their maximum teaching hours
Each staff can only teach eighteen (18) hours weekly on a basis
You can free the staff by removing several sessions
"""

#When creating new users if the selected account type is invalid,
#We will render this view

invalid_account_type = """
*******************
 INVALID CHOICE!
*******************

The user account type you selected is invalid
please check typo mistakes and try again
Available choices are

admin     =>  admin account
staff         =>  staff account
student  => student account
"""

#When loging in users, if email/password combinations are not valid,
#We will render this view

wrong_login_combination = """
*******************
 LOGIN FAILLED!
*******************

Wrong username/password combinations
please check typo mistakes and try again
"""

#When creating new items if the name has already been used,
#We will render this view

no_name = """
*******************
 NAME TAKEN!
*******************

An item with the name you provided exists
please try again with a different name
"""

#When creating new items if the slug has already been used,
#We will render this view

no_slug = """
*******************
 SLUG TAKEN!
*******************

An item with the slug you provided exists
please try again with a different slug
"""

#When displaying item profile,
#If the field in config file is not found in the sql returned data,
#We will rendor this error view

table_field_not_found = """
========================
Field not found!
========================

Once of the item profile data is missing!
Contact the administrator to fix this issue...
"""

#When assigning new items to users,
#If the item has already been assigned,
#We will rendor this error view

item_assigned = """
========================
Item Found
========================

This item has already been assigned to this user!
Check typo mistakes and try again or try assigning another item...
"""

#When displaying module sessions,
#If no sessions are found for current module,
#We will rendor this error view

no_session = """
========================
NO SESSIONS FOUND!
========================

There are no sessions for this module

To create new sessions for this module, you can use;

[ create -s]

you can also parse as many arguments as you want
Use -h -s to see available arguments

"""

#When displaying courses,
#If no modules are found for current course,
#We will rendor this error view

no_module = """
========================
NO MODULES FOUND!
========================

There are no modules for this course

To create new modules for this course, use;

[ create -m]

you can also parse as many arguments as you want
Use -h -m to see available arguments

"""

#When displaying users data,
#If current user has no courses/modules,
#We will rendor this error view

no_course = """
========================
No Courses Found
========================

There are no courses found for this user,
if this user is a student, you can use [assign] comand
to assign new courses.
If this account is admin, there is nothing to worry about
"""

#When assigning new items to users,
#If the item has already been assigned,
#We will rendor this error view

no_comand = """
========================
Comand Not Found
========================

This comand cannot be used on this item
Use -h [comand] to see available options
"""


