#----1----

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = int(input('1 - Enter a number'))
print("    The factorial of", num, "is", factorial(num))


#----3----

def filter(function, iterable):
    result = []
    for i in iterable:
        if function is None:
            if i:
                result.append(i)
        else:
            if function(i):
                result.append(i)
    return result


def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(is_even, numbers)
print('3 - ',filtered_numbers)


#----4----
def power_of_four(number):
    if number <= 0:
        return False
    while number > 1:
        if number % 4 != 0:
            return False
        number /= 4
    return True

print(power_of_four(int(input("4 - Enter a number"))))
