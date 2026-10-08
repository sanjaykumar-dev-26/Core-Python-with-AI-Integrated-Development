'''
Write a python program:
- read an app name from <STDIN>
- test - flask -> initialize port number is 5000
- test - fastAPI -> initialize port number is 8080
- test - prometheus ->initialize port number is: 9090
|
-default app name is: web2.0 and port number 8000
|
- display app name and running port number
'''

app_name=input("Enter app name: ")

if(app_name=="flask"):
    port=5000
elif(app_name=="fastAPI"):
    port=8080
elif(app_name=="prometheus"):
    port=9090
else:
    app_name="web2.0"
    port=8000

print(f"App Name is: {app_name} Running on Port: {port}")
