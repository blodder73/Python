sampleText = "Python is very powerful language"
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
