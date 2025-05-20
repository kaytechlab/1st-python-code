#Write a function grade_category(score) that takes a student’s score (between 0–100) and returns the grade:
#90+: "A"
#80–89: "B"
#70–79: "C"
#60–69: "D"
#Below 60: "F"

score=[100,99,92,90,81,87,78,77,69,65,59,53,54,45,43,42,39,20,60,59,24]
def grade_category(score):
    if score  >=90:
        print("A")
    elif score >=80 and score <90:
        print("B")
    elif score >= 70 and score <80:
        print("C")
    elif score >= 60 and score <70:
        print("D")
    elif score >=50 and score <59:
        print("F")
    else:
        print("F")
for grade in score:
    grade_category(grade)
    print(grade)

#Then, write another function categorize_grades(scores) that takes a list of scores and returns
# a dictionary of how many students got each grade.

def categorize_grades(scores):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score >= 50:
        print("F")

dictionary = {
    90:"A",
    80: "B",
    70: "C",
    60: "D",
    50: "F",
}
print(dictionary)