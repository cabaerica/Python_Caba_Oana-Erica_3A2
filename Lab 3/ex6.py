def list_op(list):
    a = [value for value in list if list.count(value) == 1]
    b = len(list) - len(set(list))
    return (len(a), b)

print(list_op((1, 3, 5 , 6 , 5 , 100, 200, 100, 100, 200)))