import pypdf as pd
import os

merge = pd.PdfMerger()

files = os.listdir("C:\\Programming\\Python\\xavier\\data\\tut 1")
for f in files:
    if f.endswith(".pdf"):
        print(f)
        merge.append(os.path.join("C:\\Programming\\Python\\xavier\\data\\tut 1",f))

merge.write("combined.pdf")
merge.close()