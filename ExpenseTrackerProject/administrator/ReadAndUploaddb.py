import pandas as pa

class ImportExcelAndLoad:
 
    def __init__(self):
        self.df = ""

    def ImportExcel(self):
        self.df = pa.read_excel(r"D:\\MyRepo\\ExpenseTracker\\ExpenseTrackerProject\\administrator\\Static\\Data\\Flat_Expense.xlsx")
        print(self.df)