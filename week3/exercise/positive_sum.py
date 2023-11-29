def positive_sum(numbers):
    return sum(i for i in numbers if i > 0)

numbers = [1, -2, 3]
print(positive_sum(numbers))  