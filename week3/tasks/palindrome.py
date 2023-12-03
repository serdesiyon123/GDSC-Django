word = str(input("Enter a word: "))

word.lower()
if word == word[::-1]:
    print(1)
else:
    print(0)