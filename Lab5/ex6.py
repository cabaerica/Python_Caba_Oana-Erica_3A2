def function(args):
    return list(zip(list(filter(lambda x: x % 2 == 0, args)), list(filter(lambda x: x%2 == 1, args))))

print(function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))