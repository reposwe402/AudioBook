import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a single string.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text_list = []
        for page_num in range(pdf_reader.numPages):
            try:
                page = pdf_reader.getPage(page_num)
                text_list.append(page.extractText())
            except:
                pass
        return " ".join(text_list)
