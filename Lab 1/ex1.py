import math

def cmmdc(list_of_numbers):
    if(len(list_of_numbers) < 2):
        return -1
    gcd = math.gcd(list_of_numbers[0], list_of_numbers[1])
    if(len(list_of_numbers) == 2):
        return gcd
    for n in list_of_numbers[2:len(list_of_numbers)]:
        gcd = math.gcd(gcd, n)
    return gcd

x = list(map(int, input("Enter multiples numbers to calculte their gcd: ").split()))
print(cmmdc(x))
