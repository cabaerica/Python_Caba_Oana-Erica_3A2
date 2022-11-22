import os
import re

def search_files(path, regex):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(file):
            search_files(file, regex)
        else:
            if re.match(regex, file):
                print('>>', file)
            elif re.search(regex, file):
                print(file)

def main():
    search_files("./Lab 6",r'\.py$')

main()