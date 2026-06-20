name = input("Name:")
score = int(input("Score:"))
if score >= 80:
    print("Great")
else:
    print("Needs improvement")

subjects = ["Math","Science","English"]
subjects.append("Coding")

for course in subjects:
    print(course)

print("Thank you",name)