import pandas as pa
import sqlalchemy
from sqlalchemy import create_engine
from .Static.Templates import DbTemplates

class ImportExcelAndLoad:
 
    def __init__(self):
        self.df = ""
        self.sqlcon = create_engine(r'mssql+pyodbc://@DESKTOP-RLTI3FK\ARJUNDU/DivyaUrbania?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
        self.sqlcon.connect()


    def ImportExcel(self):
        """Import excel values into a dataframe"""

        self.df = pa.read_excel(r"D:\\MyRepo\\ExpenseTracker\\ExpenseTrackerProject\\administrator\\Static\\Data\\Flat_Expense.xlsx")  


    def LoadExcel_ToDb(self):
        """Load excel data and insert the data into DB(SQL SERVER)."""

        self.ImportExcel()
        #query = DbTemplates.GetQuery('insert')
        self.df.to_sql("TBExpenseRecord", con=self.sqlcon, if_exists='append', index=False)



