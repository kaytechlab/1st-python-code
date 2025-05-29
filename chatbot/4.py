#Write a function letter_frequency(text) that returns a dictionary showing how many times each letter appears in the text (ignore spaces and count lowercase only).

text=("Far From Home")
def letter_frequency(text):
    text = text.lower()
    frequency = {}

    for char in text:
        if char == ' ':
            continue
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
print(letter_frequency("far from home"))

