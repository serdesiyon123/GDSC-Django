def positive_sum(numbers):
    return sum(i for i in numbers if i > 0)


number = list(map(int, input("Enter numbers: ").split()))
print(positive_sum(number))
