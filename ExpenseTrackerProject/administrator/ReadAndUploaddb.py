import pandas as pa
import sqlalchemy
from sqlalchemy import create_engine
from .Static.Templates import DbTemplates

class ImportExcelAndLoad:
 
    def __init__(self):
        self.df = ""
        self.conn = create_engine('mssql+pymssql://DESKTOP-RLTI3FK\ARJUNDU/DivyaUrbania')


    def ImportExcel(self):
        """Import excel values into a dataframe"""

        self.df = pa.read_excel(r"D:\\MyRepo\\ExpenseTracker\\ExpenseTrackerProject\\administrator\\Static\\Data\\Flat_Expense.xlsx")
        self.df.to_dict()    


    def LoadExcel_ToDb(self):
        """Load excel data and insert the data into DB(SQL SERVER)."""

        self.ImportExcel()
        #query = DbTemplates.GetQuery('insert')
        self.df.to_sql("TBExpenseRecord",con=self.conn,if_exists='append')



