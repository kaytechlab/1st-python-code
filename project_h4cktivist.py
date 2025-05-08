# A program to ask the correct user  or owner of the code to check for the correct department
print("Name: Ogundipe oluwaseyi damilola")
print("Matric Number: 2022/41540")
print("Dept : Information Technology")

# checking for the correct department
while True:
    try:
        dept_quest = input("Which dept are you ? ")
        if dept_quest.lower() != "information technology":
            raise ValueError("You have entered an incorrect department name. ")
        else:
            print("You are in " + dept_quest.upper(), "department")
            break
    except ValueError as e:
        print(e)
        print("Please try again!!!")


