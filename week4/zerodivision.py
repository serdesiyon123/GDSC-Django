try:
    x , y =map(int ,input("enter two nums: ").split())
    print(x / y)

except ZeroDivisionError:
    print("Can't divide by zero")
