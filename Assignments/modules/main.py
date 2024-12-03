# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# 1 
import this
#print(this)

# 2
import time
def wait(seconds):
    time.sleep(seconds)
    return None

print(wait)

# 3
import math
def my_sin(float):
    uitkomst = math.sin(float)
    return uitkomst

print(my_sin)

# 4
from datetime import datetime
def iso_now():
    my_date = datetime.now()
    return my_date.strftime("%Y-%m-%dT%H:%M")
    
print(iso_now)


# 5
import sys
def platform():
    return sys.platform

print(platform)

# 6 
from greet import supergreeting
# see new file greet.py.
def supergreeting_wrapper(name):
    greeting = supergreeting(name)
    return greeting

supergreeting_wrapper("Winc")