import re

def function1(txt):
    return re.findall("[a-z0-9]+",txt,flags=re.IGNORECASE)

def main():
    print(function1("Ana are mere. Bogdan are pere!"))

main()