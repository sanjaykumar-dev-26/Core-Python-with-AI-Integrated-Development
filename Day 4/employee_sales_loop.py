
fobj = open('C:\\Users\\Admin\\Desktop\\Core-Python-with-AI-Integrated-Development\\Day 4\\emp.csv', 'r')

L = fobj.readlines()
fobj.close()

total = 0

for var in L:
    if 'sales' in var:
        var = var.strip()
        emp_list = var.split(",")
        ecost = emp_list[-1]
        total = total + int(ecost)

print(f"Sum of sales dept emp's cost: {total}")