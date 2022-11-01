from distutils.filelist import FileList
import os
def search_in_file(target, to_search):
    if(os.path.isfile(target)):
        with open(target, "r") as f:
            file = f.read()
            if(to_search in file):
                return target
            else:
                return None
    else: return None

def f5(target, to_search):
    if(os.path.isfile(target)):
        return(search_in_file(target, to_search))
    elif(os.path.isdir(target)):
        filesList = []
        for root, dirs, files in os.walk(target):
            for f in files:
                complete_file = os.path.join(target, f)
                if(search_in_file(complete_file, to_search) == complete_file):
                    filesList += complete_file
        return filesList
    else:
        raise ValueError("Fisier/Director invalid")

print(f5(r'C:\Users\erica.caba\OneDrive - Gemini CAD Systems\Desktop', "vine valu"))