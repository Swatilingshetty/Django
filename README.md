# Django24
Django24

# Django
* Django is python based web framework used for building web applications of high quality
* its helps us to avoid repotative task, which process of web development an easy experience and save time

# How to craete virtual env in windows
* note: '''pip --version'''
  '''.
  
(swati) C:\Django24\01_projectstructure\swati\Scripts\project_test>pip --version
pip 23.2.1 from C:\Django24\01_projectstructure\swati\Lib\site-packages\pip (python 3.12)

(swati) C:\Django24\01_projectstructure\swati\Scripts\project_test>python -m pip --version
pip 23.2.1 from C:\Django24\01_projectstructure\swati\Lib\site-packages\pip (python 3.12)

(swati) C:\Django24\01_projectstructure\swati\Scripts\project_test>pip -V
pip 23.2.1 from C:\Django24\01_projectstructure\swati\Lib\site-packages\pip (python 3.12)
  '''
* create folder
* enter into folder
* open cmd from cuurent folder
* check the Django version ''' python -n django---version'''
* create vertual env*** python -n wiev env***
*  > cd env
* > cd scripts
* > activate
* '''pip install django'''
* create project '''django-admin startproject projectname'''
* > dir
** '''python manage.py runserver'''


* python manage.py startapp application
* '''pip install django'''
* create project '''django admin startproject projectName
* > cd projectname
* > dir
* '''python manage.py runserver''' 
  
## explain django project structure
'''
__init __.py: this is for python it can treated as package.
asgl.py: ASGI stands aschronous server gateway interface,
         it ends the capabilities of WSGI (web server gateway interface) which is standard way communication b/w web server and web application.
settings.py: this file contain project settings to modify function.
urls.py: this has links to you projects as well as functions to call (we apply some routing).
wsgi.py : this is needed if you want to perform deployment for your projects.
manage.py : it is mainfile for the entire project and application

'''
# Explain Django app structure
'''
__init__.py: this is for python it can treated as packege.
Admin.py: this helps to make the app modifiable in admin interface.
app.py : this is a configuration file common for all django apps.
manage.py: this will store all the models of the appliaction.
test.py: this can be used for performing the unit testing.
views.py: this is were the application logic
'''
