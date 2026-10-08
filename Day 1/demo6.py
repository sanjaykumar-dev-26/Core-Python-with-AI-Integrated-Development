'''
Write a python program 
- read a employee details(name,age,cost) from <STDIN>
- using print() - display employee details.
- calculate emp basic salary with 18% tax and display the tax
- calculate tax + basic salary and display the total salary(including tax)
'''

elogin_status = True
ename=input("Enter employee name: ")
eage=int(input("Enter employee age: "))
ecost=float(input("Enter employee cost: "))
tax = ecost * 0.18
total_salary = float(ecost) + tax

print(f'Employee Name: {ename}')
print(f'Employee Age: {eage}')
print(f'Employee Cost: {ecost}')
print(f'Employee Login Status: {elogin_status}')
print(f'Tax: {tax}')
print(f'Total Salary (including tax): {total_salary}')