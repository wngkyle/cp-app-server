import openpyxl
import pandas as pd

wb = openpyxl.Workbook()
wb.save(r"C:\Users\f0793\Desktop\test.xlsx")

fpath = r'C:\Users\f0793\Desktop\TPA001C\ES2506(CBW23080031)\ES02506-01-NTM_2023-09-28_14_41_28.xls'
fd = pd.read_excel(fpath, sheet_name=0)
print(fd)


