originalWord = input()
closestVowel = {
"b": "a",
"c": "a",
"d": "e",
"f": "e",
"g": "e",
"h": "i",
"j": "i",
"k": "i",
"l": "i",
"m": "o",
"n": "o",
"p": "o",
"q": "o",
"r": "o",
"s": "u",
"t": "u",
"v": "u",
"w": "u",
"x": "u",
"y": "u",
"z": "u",
}
newWord = ""
consonants = "bcdfghjklmnpqrstvwxyz"
for i in range(len(originalWord)):
    if originalWord[i] in consonants:
        if originalWord[i] != "z":
            newWord += originalWord[i] + closestVowel[originalWord[i]] + consonants[consonants.index(originalWord[i]) + 1]
        else:
            newWord += originalWord[i] + closestVowel[originalWord[i]] + "z"
    else:
        newWord += originalWord[i]
print(newWord)
        
