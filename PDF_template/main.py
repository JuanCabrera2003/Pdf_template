import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

data = pd.read_csv("topics.csv")
for index, row in data.iterrows():
    pdf.add_page()
 
    # Set the header
    #arguments: kind of word, style=bold
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    #arguments w=width,ln=breakline h=size same number
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Generar múltiples líneas horizontales en el PDF
    # Se dibujan desde x=10 hasta x=200, comenzando en y=20 hasta y=298,
    # con un espaciado de 10 unidades entre cada línea.
    for y in range(20 , 298, 10): # Itera valores de "y" desde 20 hasta 298 con pasos de 10
        pdf.line(10, y, 200, y)  # Dibuja una línea horizontal desde (10, y) hasta (200, y)
    

    #set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

         #set the footer
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20 , 298, 10):
            pdf.line(10, y, 200, y)
       
pdf.output("output.pdf")
