'''
Write a python program:
i. create an empty list
ii.display number of elements in the list # use len() function # -> 0
|
iii. use while loop - limit is 5
    a -> read a hostname from user input
    b -> append the hostname to the list
iv. display number of elements in the list # use len() function # ->5
|
v. use for loop - iterate through the list
|
vi. read a hostname from <STDIN>
vii. test input hostname is existing or not in the list
                             |          ===================
viii.                        modify the hostname        |__add the hostname 
                                |__last Index 
                                
ix. display the list of hostnames - use for loop

'''

host=[] 
print("Number of elements in the list:", len(host))

i=0
while i<5:
    hostname=input("Enter hostname: ")
    host.append(hostname)
    i+=1

print("Number of elements in the list:", len(host))

for h in host:
    print(h)

hostname=input("Enter a hostname to check: ")
if hostname in host:
    host[-1]=hostname
else:
    host.append(hostname)

print("List of hostnames:")
for h in host:
    print(h)

