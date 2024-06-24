from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm, inch

pdf = Canvas("new_pdf.pdf")

x_lst = [10,180,500]
y_lst = [180,140,100]

# y_columns = 185
# x_columns = 15
pdf.grid(x_lst,y_lst)
# pdf.drawString(15,70,"Hii")
# pdf.drawString(85,70,"Radha")
# pdf.drawString(15,90,"Hello")
# pdf.drawString(85,90,"Dude")

# data = [["Hii", "Radha"],["Hello ","Dude"]]
# t = Table(data)


pdf.save()