import openpyxl
import os


current_folder = os.getcwd()
file = "{}\excel\\empty.xlsx".format(current_folder)

workbook = openpyxl.load_workbook(file)
sheet = workbook["Sheet1"] # or workbook.active

# same data
for row in range(1, 6):
  for column in range(1, 4):
    sheet.cell(row, column).value = "welcome"

workbook.save(file)