# Extract data from pdf

from PyPDF2 import PdfReader
import os

def get_pdf_text(pdf_file_path: str) -> str:
    """
    Extract text from a PDF file and return it as a string.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.

     Raises:
        FileNotFoundError: If the PDF file does not exist.
        ValueError: If the file does not have a '.pdf' extension.
    """
    # Check if the file exists
    if not os.path.exists(pdf_file_path):
        raise FileNotFoundError(f"PDF file '{pdf_file_path}' not found.")
    
    # Check if the file has a '.pdf' extension
    if not pdf_file_path.lower().endswith('.pdf'):
        raise ValueError(f"Invalid file extension. The file must have a '.pdf' extension.")
    
    text = ""
    pdf_reader = PdfReader(pdf_file_path)
    
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text
