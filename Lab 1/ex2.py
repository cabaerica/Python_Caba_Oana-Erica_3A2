def num_of_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    word = word.casefold()
    for ch in word:
        if vowels.count(ch) != 0:
            count += 1
    return count

word = input("Write the word: ")
print(num_of_vowels(word))