from time import sleep as _sleep
from keyboard import is_pressed as key_is_pressed

def countdown(seconds):
    """Counts down from given amount of seconds
    
    Args:
        seconds (int): seconds to count down from
    """    
    for i in range(seconds, -1, -1):
        if i == 0:
            print('Time is up!')
            break
        print(i)
        _sleep(1)

def stopwatch(key='q'):
    """Counts up per second until key is pressed

    Args:
        key (str): Key to stop the timer. Defaults to 'q'.
    """    
    i = 0
    print(f'Stopwatch started. Press {key} to stop')
    while not key_is_pressed(key):
        _sleep(1)
        i += 1
        print(i)
