from pypdf import PdfWriter
merger= PdfWriter()

pdfs=[]
n=int(input("Enter the number of pdfs you want to merge: \n"))

for i in range(0,n):
    name=input(f"Enter the name of pdf{i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged-pdf.pdf")
merger.close()
