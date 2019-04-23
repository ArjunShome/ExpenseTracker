import pandas as pa

class importExcelAndLoad:
 
    def importExcel():
        global df
        df = pa.read_excel("Flat_Expenses.xlsx")
        print(df)