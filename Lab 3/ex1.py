def list_operation(a, b):
    intersection = [value for value in a if value in b]
    difference_a = [value for value in a if value not in b]
    difference_b = [value for value in b if value not in a]
    reunion = a + difference_b
    return (intersection, difference_a, difference_b, reunion)

print(list_operation([3, 4, 5 ,6 ,100 ,102, 101], [3, 200, 4, 6, 201, 203]))