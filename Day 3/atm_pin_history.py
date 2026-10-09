import time

def pin_test():
    fobj = open('pin_history.log', 'a')

    pin = 1234
    count = 0

    while count < 3:
        p = input('Enter a pin Number: ')
        count = count + 1

        if int(p) == pin:
            print(f'Success - {count}')
            fobj.write(
                f'Success - {count} pin input date/time: {time.ctime()}\n'
            )
            break
        else:
            fobj.write(
                f'Failed - user input pin: {p} date/time: {time.ctime()}\n'
            )

    if int(p) != pin:
        print('Pin is blocked')
        fobj.write(f'Pin is blocked - {time.ctime()}\n')

    fobj.close()


pin_test()