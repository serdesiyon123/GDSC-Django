try:
    x , y =map(int ,input("enter two nums: ").split())
    print(x / y)

except ZeroDivisionError:
    print("Cant divide by zero")
