from time import sleep as _sleep
from keyboard import is_pressed as key_is_pressed

def countdown(seconds):
    for i in range(seconds, -1, -1):
        if i == 0:
            print('Time is up!')
            break
        print(i)
        _sleep(1)

def stopwatch(key='q'):
    i = 0
    while not key_is_pressed(key):
        _sleep(1)
        i += 1
        print(i)
