names = ["Anu", "Ravi", "Uma", "Kiran", "Oscar", "Bhavya"]
vowel_names = []
for x in names:
    if x[0] in "aeiouAEIOU":
        vowel_names.append(x)
print(vowel_names)
