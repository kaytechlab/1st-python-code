#Write a function count_vowels(text) that returns the number of vowels (a, e, i, o, u) in the given text.
count_vowels=("a","e","i","o","u")

def count_vowels(text):
    vowels="aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count +=1

    return count

while True:
    vowels = input("what do you want to eat?: ")
    print(f"we got {vowels} from the input")
    if vowels.startswith("i want to eat"):
        print("we checked if vowels starts with i want to eat")
        splitted_text = vowels.split("eat")
        print(f"We split text to piece so we can just get food alone {splitted_text}")
        food = splitted_text[1]
        print(count_vowels(food))
        break

