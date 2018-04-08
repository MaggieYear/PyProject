import random
import time
#from utilspack import time_utils



def getLocalTime():
    # localtime = time.localtime(time.time())
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("current time:", localtime)
    return localtime

total_count = 0
username = input('Enter your name:')
min_num = input('Enter min number:')
max_num = input('Enter max number:')

filename = 'user-' + username + '.log'
content = '[' + username + ']'

target_number = random.randint(min_num, max_num)
content += 'correct number is ' + str(target_number)
print(target_number)

while total_count < 5:

    #current_time = time_utils.getLocalTime()
    current_time = getLocalTime()
    content += '\n' + current_time

    guess_num = input('Enter your guess number:')

    if guess_num in ['exit', 'quit']:
        print("exit")
        break

    elif guess_num == target_number:
        print('Correct!')
        content += '\n guess number:' + str(guess_num)
        content += '\n correct!'
        with open(filename, 'a+') as f:
            f.write(content + '\n')
        break


    elif guess_num >= min_num & guess_num <= max_num:
        total_count += 1

        if guess_num < target_number:
            print('Number Range ' + '[' + str(guess_num) + '-' + str(max_num) + ']')
            min_num = guess_num
        else:
            print('Number Range ' + '[' + str(min_num) + '-' + str(guess_num) + ']')
            max_num = guess_num

        print('Wrong!')
        content += '\n guess number:' + str(guess_num)
        content += '\n wrong!'
    else:
        total_count += 1
        print('Wrong!')
        print('Number Range '+ '['+ str(min_num) +'-'+ str(max_num) +']')
        content += '\n guess number:' + str(guess_num)
        content += '\n wrong!'

        with open(filename, 'a+') as f:
            f.write(content + '\n')
        content = ''
