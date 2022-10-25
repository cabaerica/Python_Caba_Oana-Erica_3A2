def num_of_occurence(string):
    list = []
    for c in string:
        list.append({'letter' : c, 'num' : string.count(c)})
    res = dict(sub.values() for sub in list)
    return dict(res)

print(num_of_occurence("Ana has apples."))