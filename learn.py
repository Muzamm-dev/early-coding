name = input("Name:")
age = int(input("Age:"))

def greet(name):
    print("Hello",name)
greet(name)

scores = [60,80,100]
scores.append(90)
for number in scores:
    print(number)

count = len(scores)
total = sum(scores)

print("Total items:",count)
print("Total scores:",total)
if total >= 300:
    print("Great!!")
else:
    print("Needs improvement")
if age >= 17:
    print("You are eligible for a driver's license")
else:
    print("You are not eligible for a driver's license yet")

def grade(scores):
    if scores >= 75:
        print(scores,"Passed")
    else:
        print(scores,"Failed")
grade(60)
grade(80)
grade(100)
grade(90)

number = 1
while number <= 5:
    print("Keep studying")
    number = number + 1
print("Thank you",name)
print("Program finished")