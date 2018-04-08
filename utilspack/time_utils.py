import time

def getLocalTime():
    # localtime = time.localtime(time.time())
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("current time:", localtime)
    return localtime

getLocalTime()