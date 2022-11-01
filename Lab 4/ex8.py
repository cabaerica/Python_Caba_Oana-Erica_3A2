import os
def f8(path):
    assert(os.path.isdir(path))
    files = []
    for f in os.listdir(path):
        if(os.path.isfile(os.path.join(path, f))):
            files += [os.path.abspath(os.path.join(path, f))]
    return files

print(f8(r'C:\Users\erica.caba\OneDrive - Gemini CAD Systems\Desktop'))
