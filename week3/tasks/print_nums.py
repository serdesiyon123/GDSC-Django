for i in range(100):
    output = print(f"0{i}", end=" ") if i < 10 else print(i, end=" ")


# or can be written as
# for i in range(100):
#  if i < 10:
#         print(f"0{i}", end=" ")
#     else:
#         print(f"{i}", end=" ")
