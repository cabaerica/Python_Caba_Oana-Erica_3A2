import os
import collections

def read_from_path(my_path):
    if os.path.isfile(my_path):
        return reversed(open(my_path))[0:20]
    elif os.path.isdir(my_path):
        list = {}
        for root, dirs, files in os.walk(my_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension in list:
                    list[extension] += 1
                else:
                    list[extension] = 1
        list = list.items()
        return sorted(list, key=lambda el: el[1], reverse=True)
        
print(read_from_path(r'C:\Users\erica.caba\OneDrive - Gemini CAD Systems\Desktop'))