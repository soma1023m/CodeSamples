#Refer to https://openpyxl.readthedocs.io/en/stable/usage.html
import openpyxl

def excel_counting():
        path="test_excel2.xlsx"
        wb_obj = openpyxl.load_workbook(path)
        sheet_obj = wb_obj.active
        allrows=tuple(sheet_obj.rows)
        print (allrows)
        print (len(allrows))
        allcols=tuple(sheet_obj.columns)
        print (allcols)
        print (len(allcols))
        for row in sheet_obj.values:
           for value in row:
             print(value)
        for row in sheet_obj.iter_rows(min_row=1, max_col=len(allcols), max_row=len(allrows), values_only=True):
           print(row)
        sheet_ranges = wb_obj['range names']
        print(sheet_ranges['D18'].value)
def main():
    excel_counting()
    

if __name__ == "__main__":
    main()
