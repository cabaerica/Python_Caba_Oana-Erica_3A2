import re

def function2(r,txt,x):
    return list(filter(lambda el:len(el)==x, re.findall(r,txt)))
                 
def main():
    print(function2("\w\d\d", "123v67t89", 3))
 
main()