"""
mystr = 'ajsdlfhadfaidh'

for (i,v) in enumerate(mystr):
    # if v == 'f':
    #    break
    if v == 'f':
        continue
    print(i,v )
else:
    print('finished')

"""

list1 = ['a','b','c']
list2 = [1,2]

new_list = []

for m in list1:
    for n in list2:
        new_list.append([m,n])
    print(new_list)
print('finished')