from fastapi import FastAPI, HTTPException
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = FastAPI()

def generate_pdf(content, filename):
    """
    Function to generate a PDF file.
    """
    pdf_file = f"{filename}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 700, content)  # Write content to PDF
    c.save()
    return pdf_file

@app.post("/generate_pdf/")
async def generate_pdf_endpoint(content: str):
    """
    Endpoint to generate PDF from content.
    """
    filename = "generated_pdf"
    pdf_file = generate_pdf(content, filename)
    return {"pdf_url": pdf_file}

@app.get("/healthcheck/")
async def healthcheck():
    """
    Endpoint to perform health check.
    """
    return {"message": "Server is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
