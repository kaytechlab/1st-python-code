#Write a function capitalize_words(sentence) that capitalizes the first letter of each word in a sentence.
sentence=("went far away")
def capitalize_words(sentence):
    words = sentence.split()
    # capitalized = [word.capitalize()for word in words]
    for word in words:

    return ' '.join(capitalized)
print(capitalize_words("went far away"))
