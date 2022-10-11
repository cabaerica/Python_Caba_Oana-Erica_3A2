import collections

s = input("Write your text: ")
s = s.lower()
s = s.replace(" ", "")
print(collections.Counter(s).most_common(1)[0])