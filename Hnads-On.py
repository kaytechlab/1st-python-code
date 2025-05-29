#Difficulty: Easy-Mid
#Concepts: Functions, Control Flow, Strings, Lists
#Task:
#Write a function grade_category(score) that takes a student’s score (between 0–100) and returns the grade:
##90+: "A"
#80–89: "B"
#70–79: "C"
#60–69: "D"
#Below 60: "F"
#Then, write another function categorize_grades(scores) that takes a list of scores
# and returns a dictionary of how many students got each grade.
score=[100,90,80,70,60,50,40,33,43,54,24]

def grade_category(score):
    if score >= 90:
        print("A")
    elif score >= 80 and score < 90:
        print("B")
    elif score >= 70 and score < 80:
        print("C")
    elif score >= 60 and score <70:
        print("D")
    elif score <= 50 and score >59:
        print("F")
    else:
        print("F")

stats = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0,
}
def grade_categorise(score):
    if score >=90:
        print("A")
        stats["A"] = stats["A"] + 1
        stats["A"] += 1
    elif score >= 80:
        print("B")
        stats["B"] = stats["B"]+1
    elif score >= 70:
        print("C")
        stats["C"] = stats["C"]+1
    elif score >= 60:
        print("D")
        stats["D"] = stats["D"]+1
    elif score <= 59:
        print("F")
        stats["F"] = stats["F"]+1
    return(stats)


dictionary = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    50: "F",
}
print(dictionary)
for grade in score:
    grade_category(grade)
    print(grade)
    print(grade_categorise(grade))
