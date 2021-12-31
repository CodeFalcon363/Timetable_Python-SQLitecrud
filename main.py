"""
*****************************************************

********************MAIN/UI MODULE*********************

We start a new session here
Once the user is logged in, they would be redirected to the welcome screen


"""

from build.users.security import login as user_login
from vendor.views.login import login_prompt as login_displays


print(login_displays.welcome_guest)
user_login.new_login()
