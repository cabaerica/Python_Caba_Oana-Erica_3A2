import math
def process_item(x):
    prime = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x%i == 0:
            prime = False
            break
    if prime: return x
    else: return process_item(x+1)

if __name__ == '__main__':
    x = int(input())
    print(process_item(x))