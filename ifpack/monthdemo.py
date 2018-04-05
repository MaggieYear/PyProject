
import time

#get localtime
now_time = time.localtime()

#month day
mday = now_time.tm_mday
#week day
wday = now_time.tm_wday  #0-6

result = "The current date is %s/%s/%s ,"%(now_time.tm_year,now_time.tm_mon,now_time.tm_mday)
#
# if mday <= 15:
#     result += 'early,'
# else:
#     result += 'late,'
#
#simple instead
result += 'early,' if  mday <= 15 else 'late,'

if wday == 0:
    result +='mon'
elif wday == 1:
    result +='tues'
elif wday == 2:
    result += 'wed'
elif wday == 3:
    result += 'thur'
elif wday == 4:
    result += 'fri'
elif wday == 5:
    result += 'sat'
elif wday == 6:
    result += 'sun'
else:
    result += 'wrong wday'

print(result)
