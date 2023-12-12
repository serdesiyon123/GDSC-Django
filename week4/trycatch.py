try:
    x , y =map(int ,input("enter two nums: ").split())
    print(x + y)
except Exception:
    print(f"can't sum string {Exception}")

finally:
    print("Here is your output")