import utils

while True:
    x = input()
    if x == 'q':
        break
    try:
        x = int(x) + 1
    except Exception as notInt:
        print("input not valid")
    else:
        print(utils.process_item(x))