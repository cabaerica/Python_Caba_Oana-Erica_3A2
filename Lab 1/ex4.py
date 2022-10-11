def convertUpperToLowerWithUnderscores(word):
    converted = ""
    for ch in word:
        if ch.isupper():
            if converted:
                converted += "_"
            converted += ch.lower()
        else:
            converted += ch
    return converted

word = input("Introduce the word to convert: ")
print(convertUpperToLowerWithUnderscores(word))