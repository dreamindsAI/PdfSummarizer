# Extract data from pdf

from io import BytesIO
from PyPDF2 import PdfReader

def get_pdf_text(pdf_content: bytes) -> str:
    """
    Extract text from a PDF file's content.

    Args:
        pdf_content (bytes): The binary content of the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        pdf_reader = PdfReader(BytesIO(pdf_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return str(e)
