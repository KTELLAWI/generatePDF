from fastapi import FastAPI, HTTPException,Request
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pdfkit

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

@app.post("/generate-pdf2")
async def generate_pdf(request: Request):
    html_content = await request.body()  # Get HTML content from the request body

    pdf_file = "generated_pdf.pdf"  # Set desired filename

    pdfkit.from_string(html_content, pdf_file)  # Generate PDF from HTML

    headers = {
        "Content-Disposition": f"attachment; filename={pdf_file}",
        "Content-Type": "application/pdf"
    }

    return Response(content=open(pdf_file, "rb").read(), headers=headers)

@app.get("/healthcheck/")
async def healthcheck():
    """
    Endpoint to perform health check.
    """
    return {"message": "Server is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
