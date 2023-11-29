def word_lengths(sentence):
    return [len(word) for word in sentence.split()]

sentence =input( "Write a a sentence: ")
print(word_lengths(sentence)) 