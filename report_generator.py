from fpdf import FPDF
from datetime import datetime

def generate_pdf_report(results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "AI Autonomous Web Testing Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, f"Generated On: {datetime.now()}", ln=True)
    pdf.ln(5)

    for key, value in results.items():
        pdf.multi_cell(0, 8, f"{key}: {value}")

    filename = f"report_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    pdf.output(filename)

    return filename