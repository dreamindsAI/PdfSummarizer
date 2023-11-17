from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from operations.pdf_reader import get_pdf_text
import uvicorn

# Create an instance of the FastAPI class
app = FastAPI()

# Define a simple route that responds to GET requests
@app.get("/")
def read_root():
    return {"Server is running.."}

@app.post("/pdf/")
async def upload_pdf(file: UploadFile) -> dict:

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Please upload a PDF file."}

    pdf_content = await file.read()
    
    # Process the PDF using get_pdf_text function
    text = get_pdf_text(pdf_content)

    return {"text": text}

if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
