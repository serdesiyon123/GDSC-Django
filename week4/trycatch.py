try:
    x , y =map(int ,input("enter two nums: ").split())
    print(x + y)
except Exception as e:
    print(f"can't sum string {e}")

finally:
    print("Here is your output")