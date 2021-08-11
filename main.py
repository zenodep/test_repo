from time import sleep as _sleep

def countdown(seconds):
    for i in range(seconds, -1, -1):
        if i == 0:
            print('Time is up!')
            break
        print(i)
        _sleep(1)
