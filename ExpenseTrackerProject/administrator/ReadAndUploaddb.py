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


    def BuildQuery(self,parameter):
        "Build Query To Fetch Data Fron DB"

        if parameter != "":
            if isinstance(parameter,str):
                self.column = "Item"
                self.querytype = "fetch_WithCondition"
        else :
            self.querytype = "fetchAll"
        table = DbTemplates.GetTable("data")
        dbquery = DbTemplates.GetQueryRecords(self.querytype).format(TableName = table,ColumnName = self.column,Value = "'" + parameter + "'")
        return dbquery
    

    def GetRecords_FromDB(self,parameter):
        """Fetch Records From DB"""
        
        query = self.BuildQuery(parameter)
        self.df = pa.read_sql_query(query,con=self.sqlcon, index_col = None)
        return self.df.to_dict()
