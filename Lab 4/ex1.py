import os

def files_extension(director):
    extensions = []
    for filename in os.listdir(director):
        f = os.path.join(director, filename)
        if(os.path.isfile(f) and (os.path.splitext(filename)[1] not in extensions)):
            extensions.append(os.path.splitext(filename)[1])
    extensions.sort()
    return extensions           

print(files_extension(r'C:\Users\erica.caba\OneDrive - Gemini CAD Systems\Desktop'))