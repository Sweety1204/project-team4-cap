from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class Sales():
    month:str
    sales:int
S=[Sales('jan',2345),Sales('feb',123),Sales('mar',5463573),Sales('apr',1212),Sales('may',4356)]
data=[[s.month,s.sales]for s in S]
data=[['month','sales']]+data
total=
for d in data:
    sheet.append(d)
wb.save('..//data/dtclassdemo.xlsx')