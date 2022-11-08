def vowels(string):
    return [ch for ch in string if ch.lower() in "aeiou"]

anon = lambda string: [ch for ch in string if ch.lower() in "aeiou"]

def vowels_filter(string):
    return list(filter(lambda x: x.lower() in "aieou", string))

print(vowels("Programming in Python is fun"))
print(anon("Programming in Python is fun"))
print(vowels_filter("Programming in Python is fun"))