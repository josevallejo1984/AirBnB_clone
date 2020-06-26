#!/usr/bin/python3
"""Create class BaseModel that defines all common 
attributes/methods for other class
"""
import uuid
from datetime import datetime
import os.path, time

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d,%m,%Y, %H,%M,%S")
# dd/mm/YY H:M:S format
print("s2:", s2)
a = datetime.now().strftime("%Y, %m, %d, %H, %M, %S, %f")
print(a)


first_time = str(datetime.now())
#
second_time = datetime.now()

# Outputting:
print('Second datetime.now() value: %s' % second_time)
print('First datetime.now() value: %s' % first_time)



print("created: %s" % time.ctime(os.path.getctime('test.txt')).strftime("%Y, %m, %d, %H, %M, %S, %f"))
print("last modified: %s" % time.ctime(os.path.getmtime('test.txt')).strftime("%Y, %m, %d, %H, %M, %S, %f"))