import os

def files_with_certain_letter(director, file, letter):
    w = open(file, "w")
    for filename in os.listdir(director):
        f = os.path.join(director, filename)
        if filename[0] == letter:
            w.write(f + '\n')
    w.close()

files_with_certain_letter(r'C:\Users\erica.caba\OneDrive - Gemini CAD Systems\Desktop', 'input.txt','A')