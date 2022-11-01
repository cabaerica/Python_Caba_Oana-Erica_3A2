import sys
import os

def f4():
    if(not os.path.isdir(sys.argv[1])):
        return 0
    else:
        ext = set()
        for f in os.listdir(sys.argv[1]):
            if(os.path.isfile(os.path.join(sys.argv[1], f)) and os.path.splitext(f)[1] != ""):
                ext.add(os.path.splitext(f)[1])
        return sorted(list(ext))

print(f4())