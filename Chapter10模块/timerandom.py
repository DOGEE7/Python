from time import *
from random import *
date1=(2017,1,1,0,0,0,-1,-1,-1)
time1=mktime(date1)
date2=(2018,1,1,0,0,0,-1,-1,-1)
time2=mktime(date2)
random_time=uniform(time1,time2)
local_random_time=localtime(random_time)
print(local_random_time)
print(asctime(local_random_time))
