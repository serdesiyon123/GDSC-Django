add = 0
i = 0
addt = 0
addf = 0
count = 0
while (i <= 50):
    add += i
    i += 2
    if i % 3 == 0:
        print(f"{i} Three")
        addt += i 
        count += 1
    elif i % 5 == 0:
        print(f"{i} Five")
        addf += i
        count += 1
    
       
    
print(f"Sum even numbers from 1 to 50 is: {add}")
print(f"Number of 3s and 5s:  {count} ")
print(f"Sum of of 3s and 5s:{addf + addt}")