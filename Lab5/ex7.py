def process(**kwargs):
    fib = [0, 1]
    for i in range(2, 1000):
        fib.append(fib[i - 1] + fib[i - 2])

    if 'filters' in kwargs:
        fib = list(filter(lambda x: all(predicate(x) for predicate in kwargs['filters']), fib))

    if 'offset' in kwargs:
        fib = fib[kwargs['offset']:]

    if 'limit' in kwargs:
        fib = fib[:kwargs['limit']]

    return fib

def sum_digits(x):
    return sum(map(int, str(x)))

print(process(
filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
limit=2,
offset=2))
