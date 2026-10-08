'''
Write a python program:
|-> read a appName from <STDIN>
|
|->test - using membership test flask is running -> port = 5000
				|___ not running -> port = 8080

|->display - app name and running port number
'''
app_name=input("Enter app name: ")
if app_name in 'crm  application ruuning in flask web app':
    port = 5000
else:
    port = 8080

print(f'App Name is: {app_name} Running on Port: {port}')
