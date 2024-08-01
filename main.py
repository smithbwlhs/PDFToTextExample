from PyPDF2 import PdfReader

file = open("input_files/APCSA_MC.pdf", "rb")
reader = PdfReader(file)

num_pages = len(reader.pages)

for p in range(2,num_pages):
    page = reader.pages[p]
    text = page.extract_text()
    f = open(f"output_files/APCSA_MC{p-1}.txt", "x")
    try:
        f.write(text)
    except FileExistsError:
        print("File already exists")
    f.close()