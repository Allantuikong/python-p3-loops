#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    return [num ** 2 for num in int_list]

test_list = [1, 2, 3, 4, 5]
result = square_integers(test_list)
print(result)




def fizzbuzz():
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

fizzbuzz()