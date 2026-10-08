# Copy file content using read() and write()

fobj = open('r1.log', 'r')
wobj = open('r3.log', 'w')

s = fobj.read()
wobj.write(s)

fobj.close()
wobj.close()


# Using with: Context Manager

with open('r1.log', 'r') as fobj:
    with open('r4.log', 'w') as wobj:
        L = fobj.readlines()

        for var in L:
            wobj.write(f"data -> {var}")

print("End of the line")