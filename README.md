# Profil_Software_recruiting_task
Kamil Sterniuk
sterniukkamil@gmail.com

TENNIS COURT RESERVATION SCRIPT

Used libraries:

datetime - to operate on the date variables.

json, csv - to save files in both of these formats

HOW TO USE:

After launching the script you will get directly into menu 
with 5 options:

1. Make a reservation- User is able to input name, date
of reservation and its duration. Script checks few conditions:

- Does date have a valid format.
- Is reservation made over 1 hour before.
- Do user have more than 2 reservations one week.

If the time, that user chose is unavailable, script gives user
next available hour.

2. Cancel a reservation- User should input his name and date
of reservation that he would like to cancel.

Script checks if the reservation for this conditions exists and
if it's more than an hour from now.

3. Print schedule- User gives a start and end date of reservations
that he would like to print on the screen.

4. Save schedule to a file- User can save the schedule to a file by
the date start and end for the file format he will choose (csv/json)

5. Exit- Script turns off
