import pandas as pa

class importExcelAndLoad:
 
    def __init__(self):
        self.df = ""

    def importExcel(self):
        self.df = pa.read_excel(r"D:\\MyRepo\\ExpenseTracker\\ExpenseTrackerProject\\administrator\\Static\\Data\\Flat_Expenses.xlsx")
        print(self.df)