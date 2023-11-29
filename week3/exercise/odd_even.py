x = 1
while x!=0 : 
    x = int(input("Enter a number: "))   
    if x==0:
        break
    if x % 2 == 0:
      print("Even")
    elif x % 2 != 0:
     print("Odd")
