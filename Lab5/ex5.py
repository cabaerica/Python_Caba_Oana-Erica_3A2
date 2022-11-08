def function(arg):
    return list(filter(lambda x: type(x) == float or type(x) == int, arg))

print(function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))