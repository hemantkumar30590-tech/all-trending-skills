from fpdf import FPDF
import os
for i in range(1,6):
    txt=f"cspdcl_output/CSPDCL_JE_Electrical_2026_Set_{i}.txt"
    pdf=FPDF(); pdf.add_page(); pdf.set_font("Arial", size=10)
    with open(txt,encoding="utf-8") as f:
        for line in f: pdf.cell(0,5,line[:90],ln=True)
    pdf.output(f"cspdcl_output/Set_{i}.pdf")
    print(f"PDF bana: Set_{i}.pdf")
