def num_of_ones(n):
    converted_bin = bin(n)
    count = 0
    for ch in converted_bin:
        if ch == '1':
            count += 1
    return count

print(num_of_ones(24))