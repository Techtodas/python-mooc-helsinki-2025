# Write your solution here
number = int(input("How many points [0-100]: "))

if number % 3 == 0 and number % 5 == 0:
    response = 'FizzBuzz'
elif number % 5 == 0:
    response = 'Buzz'
elif number % 3 == 0:
    response = 'Fizz'

print(response)