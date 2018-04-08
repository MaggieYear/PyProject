
"""
try:
    int('ddd')
    pass
except ValueError as e:
#except:
    print('exept',e)
    pass
else:
    print("else")
finally:
    print('finally')
"""

#raise TypeError


class myException(Exception):
    print("myException")
    pass

raise myException