# sqlite3_crud
SQLITE3 CRUD Shell
# Python 3.9

# USAGE
Clone the repo from github

git clone https://github.com/cespavtech/sqlite3_crud

cd sqlite3_crud

main.py

# COMANDS
SYNTAX

[comand] [-item] [-key] [value]<br>
The second argument after the comand will be assummed to be the item key when used with<br>
show, update or delete comand

<h4>[-item]</h4>
This is the item which the comand [comand] would run for (e.g. Users, Courses etc)<br>
It can be any of the following

-u for User (staffs, students, admins)<br>
-c for Course<br>
-m for Module<br>
-r for Rooms<br>
-s for Semester<br>

<h4>[-key]</h4>

This is a reference of the data associated with the item (e.g. -ue for user email)<br>
It can be any fo the following depending on the item used with

<h4>-u</h4>
-ue for user email<br>
-ui for user ID<br>
-un for user names<br>
-up for user password<br>
-ua for user account type (e.g. -ua staff)<br>
-uri for user room ID<br>
-urs for user room slug<br>

<h4>-c</h4>
-cs for course slug<br>
-ci for course ID<br>
-cn for course name<br>
-css for course semester slug<br>
-csi for course semester ID


<h4>-m</h4>
-ms for module slug<br>
-mi for course ID<br>
-mn for module name<br>
-mcl for module course slug<br>
-mci for module course ID

<h4>-r</h4>
-rs for room slug<br>
-ri for room ID<br>
-rn for room name

<h4>-s</h4>
-ss for semester slug<br>
-si for semester ID<br>
-sn for semester name


[comand]

Can be any of below

<h4>show</h4>

Display specific item data (no analysis)<br>
<h4>Examples</h4>
show -u -ue example@mail.com<br>
Above comand will display data for user with email address example@mail.com<br>
show -c -ci 3<br>
Above comand will display data for course with id 3 in the dabase table

<h4>report</h4>

Display analitical overview ot specific item<br>
<h4>Examples</h4>
report -u -ue example@mail.com<br>
Above comand will display report for user with email exmaple@mail.com<br>
This report includes, % of attended modules/sessions hours for students and workload for staffs

<h4>update<h4>

Update specific item's data<br>
Please remember the first argument is used to refer to item (-ue to update user data using email)
<h4>Examples</h4>
update -u -ue example@mail1.com -un Abdirahim Abdi -ua staff<br>
Above comand will update names and account type of user with email address example1.com

  <h4>create</h4>

Create new item<br>
<h4>Examples</h4>
create -u -ue example@mail.com -un Abdirahim Abdi -ua student -urs r_1 -up password<br>
Above comand will create a new student account if no user with example@mail.com email address is found!<br>
Keep close look at how we passed other arguments, all arguments are optional except -ue (email address)<br>
If a value is missing and required, you will be prompted to enter it

<h4>delete</h4>

Delete an item<br>
<h4>Examples</h4>
delete -u -ue example@mail.com -force<br>
This example will delete a user with email address example@mail.com<br>
If the -force argument is not passed, you will be prompted to confirm user deletion along with the user's data (e.g. names)

<h4>assign</h4>

Assign an item to other item (e.g. module to course or course to semester)<br>
<h4>Examples</h4>
assign -c -ue example@mail.com -cs web_dev<br>
Above example will assign the course with slug web_dev to user with email address example@mail.com<br>
assign -m -mi 3 -cs sem_ce2<br>
Above comand will add module with id 3 to course with slug sem_c2

# HELP
  
use -h to display this docs on your terminal<br>
or use -h comand to display help/doc about specific comand<br>
<h4>Examples</h4>
-h create<br>
Will display possible usage for comand create



