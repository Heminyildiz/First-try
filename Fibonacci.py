fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
point = 5
input('*****Press ENTER to start*****')
name = input("NickName: ")
print(f"Dear {name}, lets play game!")

print("Fill in the spaces marked with '*' below.")

print(f"0 1 '*' 2 3 5 '*' 13 21 '*' 55")


number = input("1st number: ")
if number == "1":
    print(f"True!\n{point} pts!!\n")
else:
    print("False!\n")

number = input("2nd number: ")
if number == "8":
    print(f"True!\n{point} pts!!\n")
else:
    print("False!\n")

number = input("3rd Number: ")
if number == "34":
    print(f"True!\n{point} pts!!\n")
else:
    print("False!\n")

print(f"Congratulations! Game is complete.")

print("*" *50)
input('*****Press ENTER to start new game*****')
print("*" *50)
print("Lets start new games")

print("Q1.Where is the capital of Turkey?")
answer = input("Your answer: ")
if (answer == "Ankara") or (answer == "ankara"):
    print(f"True!\n{point} pts!!\n")
else:
    print("False!\n")

print("Q2.Which team won the UEFA trophy in 2000?")
answer = input("Your answer: ")
if (answer == "Galatasaray") or (answer == "galatasaray"):
    print(f"True!\n{point} pts!!\n")
else:
    print("False!\n")

print("Q3.Which is not an element?")
print("a.nitrogen\nb.water\nc.oxygen")
answer = input("Your answer: ")
if (answer == "water") or (answer == "b") or (answer == "Water"):
    print(f"True!\n{point} pts!!\n")
else:
    print("False!\n")
print(f"Congratulations! All games are complete.")

input('*****Press ENTER to exit*****')
