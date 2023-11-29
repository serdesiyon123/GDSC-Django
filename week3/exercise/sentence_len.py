def sentence_size():
    enter = str(input("enter a sentence: "))
    if len(enter) >= 10:
        print("Long")
    else:
        print("short")
        
sentence_size()