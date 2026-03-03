# Write your solution here
temperature = int(input("Please type in a temperature (F):"))
cel = 5/9*(temperature-32)
print(f"{temperature} degrees Fahrenheit equals {cel} degrees Celsius")
if cel < 0:
    print("Brr! It's cold in here!")