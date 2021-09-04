# Instawork full-stack assignment

Simple team member management application that allows to view, edit and delete team members

## List page
- Shows a list of team members
- Reflects the number of team members on subtitle
- Lists admin team members next to their name
- Goes to edit page when a team member is clicked
- Goes to add page when + at the top is clicked

## Add page
- Receives team member info (first & last name, phone number and e-mail) and role (regular - default or admin)
- Goes to list page when save is clicked

## Edit page
- Modifies team member info and role
- Goes to list page upon team member storage when save is clicked
- Goest to list page upon team member removal when delete is clicked

![Image of team member management](/images/team_member_management.PNG)

> **_NOTE:_**  Besides Python and Django installation,
              the following packages are needed:
              *django-phone-field* for phone number
              field and *pillow* for image field.
