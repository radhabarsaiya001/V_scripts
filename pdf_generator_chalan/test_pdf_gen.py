from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.units import cm, inch

file_name = "chalan.pdf"
documentTitle = "docs/chalan"

# required page size = 5X7 inches.

# ***************pdf generate**************
pdf = Canvas("chalan.pdf", pagesize=(5 * inch, 7 * inch))

# **********title set of docs**************
pdf.setTitle(documentTitle)

# # ***********draw image in particuler position************
pdf.drawInlineImage('resized_car_image.jpg',35,320)
pdf.drawInlineImage('resized_num_plae.jpg',55,260)
pdf.setFont("Times-Roman", 24)
pdf.drawString(62,62,"Hii Radha")
pdf.setFont("Times-Bold", 20)
pdf.drawString(76,76,"Hii Dood")

pdf.save()
