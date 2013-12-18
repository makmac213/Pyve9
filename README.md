Pyve9
=====

Python Five9


Setup
=====

Open the settings.py file and edit the username, password and email with
your Five9 credentials.

Usage
=====

five9 = Five9()

skills = five9.client.service.getSkills()

print skills

