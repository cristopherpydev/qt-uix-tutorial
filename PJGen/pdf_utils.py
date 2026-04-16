from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
def generate_rpg_pdf(data,path):
    '''path is the chosen directory'''
    name, race, char_class, alignment, background, level, backstory = data #unpacking data from list dataset   
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    parchment_color = HexColor('#FDF5E6')  
    border_color = HexColor('#8B4513')    
    text_color = HexColor('#2F4F4F')    

    c.setFillColor(parchment_color)
    c.rect(0, 0, width, height, fill=1)

    c.setStrokeColor(border_color)
    c.setLineWidth(3)
    c.rect(20, 20, width-40, height-40, fill=0)
    c.setLineWidth(1)
    c.rect(25, 25, width-50, height-50, fill=0)

    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(border_color)
    c.drawCentredString(width/2, height - 80, "BASIC 5E CHARACTER SHEET")
    
    c.line(100, height - 90, width - 100, height - 90)

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(text_color)
    
    y_start = height - 140
    c.drawString(60, y_start, f"NAME: {name.upper()}")
    c.drawString(60, y_start - 30, f"RACE: {race}")
    c.drawString(60, y_start - 60, f"CLASS: {char_class}")
    
    c.drawString(350, y_start, f"LVL: {level}")
    c.drawString(350, y_start - 30, f"ALIGNMENT: {alignment}")
    c.drawString(350, y_start - 60, f"BACKGROUND: {background}")

    c.setStrokeColor(border_color)
    c.roundRect(60, 60, width - 120, height - 320, 10, stroke=1, fill=0)
    
    c.setFont("Helvetica-Oblique", 16)
    c.drawString(70, height - 260, "A dawn of a legend:")
    
    c.setFont("Times-Roman", 12)
    text_obj = c.beginText(80, height - 290)
    text_obj.setLeading(14)
    
    wrapped_text = backstory.replace('\n', '<br/>') 
    lines = [backstory[i:i+85] for i in range(0, len(backstory), 85)]
    
    for line in lines:
        text_obj.textLine(line)
    c.drawText(text_obj)

    # --- FOOTER ---
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(width/2, 40, "May dices be with you.")

    c.save()
