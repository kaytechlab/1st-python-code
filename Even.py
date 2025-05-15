#Write a function extract_evens(numbers) that takes a list of numbers
# and returns a new list with only the even numbers.
numbers=[1,5,6,8,9,12,15,7,6]
def extract_evens(numbers):
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
print(extract_evens([1,5,6,8,9,12,15,7,6]))


