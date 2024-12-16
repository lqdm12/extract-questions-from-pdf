import fitz  # PyMuPDF

pdf_path = "QUIMICA-1.pdf"  # Replace with your PDF file
output_file = "questions.txt"

doc = fitz.open(pdf_path)
with open(output_file, "w", encoding="utf-8") as f:
    for page in doc:
        text = page.get_text()
        f.write(text)
print("Questions extracted to questions.txt")
