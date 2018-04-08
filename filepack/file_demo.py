"""

#open file
f = open('record.txt','r+')

#write to file
#f.write('hello Jan')

#read file
print(f.readline())

#close
f.close()

with open('record.txt','r+') as fin:
        print(fin.readline())

        fin.close()

"""


while True:
        mystr = input('Enter info:')
        print(mystr)

        filename = 'record.txt'

        if mystr in ['exit','quit']:
                print("exit")

                with open(filename, 'r+') as f:
                        for v in f:
                                print(v)
                f.close()
                break
        else:
                print("continue")
                f = open('record.txt', 'a+')
                f.write(mystr + '\n' )
                # with open('record.txt', 'a+') as f:
                #         f.write(mystr + '\n' )

                with open(filename, 'r+') as f:
                        for v in f:
                                print(v)
                f.close()
                print('finished')
                f.close()



