from pypdf import PdfReader

def read_pdf(uploaded_file):
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text