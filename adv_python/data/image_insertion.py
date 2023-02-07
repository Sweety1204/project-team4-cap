from openpyxl import load_workbook
from openpyxl.drawing.image import Image
workbook=load_workbook(filename='..//data/newsheet.xlsx')
sheet=workbook.active
logo=Image('..//data/q1-Himasree.png')
logo.height=150
logo.width=150
sheet.add_image(logo,'D10')
workbook.save(filename='..//data/q1-Himasree.xlsx')