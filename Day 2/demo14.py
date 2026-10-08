'''
Given List

Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

-> iterate a emp list
-> split each element of the list using ',' as a delimiter
-> display empName in title case and emp department in upper case 
-> calculate sum of emp salary and display the total salary
'''


total_salary=0
Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']
for emp in Emp:
    eid,ename,dept,ecost=emp.split(',')
    print(f"Employee Name: {ename.title()}, Department: {dept.upper()}")
    total_salary+=int(ecost)
print(f"Total Salary: {total_salary}")