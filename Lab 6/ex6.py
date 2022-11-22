import re

def censor_words(text):
    words = []
    word = ''
    for i in text:
        if i.isalnum():
            word += i
        else:
            if word != '':
                words.append(word)
            word = ''
    if word != '':
        words.append(word)

    censored_words = list()
    for i in words:
        if re.match('[aeiouAEIOU]', i[0]) and re.match('[aeiouAEIOU]', i[-1]):
            censored_word = ''
            for j in range(len(i)):
                if j % 2 == 0:
                    censored_word += i[j]
                else:
                    censored_word += '*'
            censored_words.append(censored_word)
    return censored_words

def main():
    text = "Ana are mere si afine"
    words = censor_words(text)
    print(words)

main()