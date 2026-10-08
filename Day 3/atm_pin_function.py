import time


def pin_test(arg):
    pin = 1234

    if int(arg) == pin:
        return 1

    return 0


for var in range(3):
    p = input('Enter a pin Number: ')

    if pin_test(p):
        print(
            f'Success - input pin is matched '
            f'entry date/time: {time.ctime()}'
        )
        break
    else:
        print(
            f'Sorry input pin number is not matched: '
            f'date/time: {time.ctime()}'
        )

else:
    print(f'PIN is blocked - date/time: {time.ctime()}')