

def isComplete(number):

    sum = 0
    for n in range(1, number):
        if (number % n) == 0:
            sum += n
    print(sum)
    if sum == number:
        return True
    return False

number = input('Enter number:')
result = isComplete(number)

print(result)
