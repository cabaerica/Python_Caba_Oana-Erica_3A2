def function(*args, **kwargs):
    dicts = list(filter(lambda x: type(x) == dict and len(x) >= 2 and any([True if type(key) == str and len(key) >= 3 else False for key in x.keys()]), args))
    dicts += list(filter(lambda x: type(x) == dict and len(x) >= 2 and any([True if type(key) == str and len(key) >= 3 else False for key in x.keys()]), kwargs.values()))
    return dicts



print(function({1: 2, 3: 4, 5: 6}, 

 {'a': 5, 'b': 7, 'c': 'e'}, 

 {2: 3}, 

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}))