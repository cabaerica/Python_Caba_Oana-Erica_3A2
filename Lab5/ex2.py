def sum_values(*args, **kwargs):
    sum = 0
    for arg in kwargs.keys():
        sum += int(kwargs[arg])
    return sum

anon = lambda *args, **kwargs: sum([arg for arg in kwargs.values()])

print(sum_values(1, 2, c=3, d=4))
print(anon(1, 2, c=3, d=4))