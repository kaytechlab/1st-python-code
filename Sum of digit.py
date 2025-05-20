#Write a function sum_of_digits(number) that returns the sum of all digits in a string number.
numbers=[2,32,3,2,4,5,7,3,5]
def sum_of_digits(number):
    count = 0

    for num in numbers:
        count += int(num)

    return count
print(sum_of_digits(numbers))
print(sum_of_digits("numbers"))

