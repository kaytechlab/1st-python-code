#Write a function find_max(numbers) that returns the largest number in a
# list without using the built-in max() function.
numbers = [50,2,4,7,90,4,8,15,34,5,7,20]
def find_max(numbers):
    max = 0
    for i in numbers:
        if i > max:
            max = i
    return max
print(find_max(numbers))
print(find_max([73,45,123, 23, 4]))
print([])

def print_nil():
    return "kay!!"

print(print_nil())