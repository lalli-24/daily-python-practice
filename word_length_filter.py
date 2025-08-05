# Filters words longer than 4 characters from a sentence using list comprehension

sentence = input("Enter a sentence you like: ")
a = sentence.split()
b = [x for x in a if len(x) > 4]
print(b)
