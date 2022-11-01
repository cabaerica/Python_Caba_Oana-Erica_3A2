import os

def f7(path):
    if(not os.path.isfile(path)):
        raise ValueError("Calea nu duce spre un fisier")
    else:
        return {"full_path": os.path.abspath(path),
                "file_size": os.path.getsize(path),
                "file_extension": os.path.splitext(path)[1],
                "can_read": os.access(path, os.R_OK),
                "can_write": os.access(path, os.W_OK) }

print(f7(r'C:\Users\erica.caba\OneDrive - Gemini CAD Systems\Desktop\Alma.bmp'))