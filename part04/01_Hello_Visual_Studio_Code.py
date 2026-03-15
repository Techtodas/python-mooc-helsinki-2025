# Write your solution herewhile True:
while True:
    editor = input("Editor: ")
    if "visual studio code" == editor.lower():
        print("an excellent choice!")
        break
    elif "word" == editor.lower():
        print("awful")  
    else:
        print("not good")
