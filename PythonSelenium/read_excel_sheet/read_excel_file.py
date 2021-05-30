import openpyxl


filepath  = "E:\\15feb2021\\PythonSelenium\\read_excel_sheet\\test_data.xlsx"

wb = openpyxl.load_workbook(filepath)

sheets = wb.worksheets
print(sheets)

print(sheets[0]._get_cell(1, 1).value)

print(sheets[0]._get_cell(2, 1).value)

print(sheets[0]._get_cell(2, 2).value)


def get_cell_data(row, col, filepath=filepath):
    wb = openpyxl.load_workbook(filepath)
    sheets = wb.worksheets
    return sheets[0]._get_cell(row, col).value


#print(get_cell_data(1, 2))

#cell =

#print(cell.value)
