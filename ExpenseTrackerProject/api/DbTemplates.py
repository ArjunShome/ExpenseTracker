from sqlalchemy import create_engine
import pandas as pa


def CreateConnection():
    sqlcon = create_engine(r'mssql+pyodbc://@DESKTOP-RLTI3FK\ARJUNDU/DivyaUrbania?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    sqlcon.connect()
    return sqlcon

def GetQuery(command):
    """Gives the Query template to the user for the required db command."""

    QueryTemplate = {
        "update":"UPDATE {table} SET {column} = {value} WHERE {condition}",
        "delete":"DELETE FROM {table} WHERE {condition}",
        "select":"SELECT {columns} FROM {table} WHERE ",
        "select_all":"SELECT {columns} FROM {table}",
        "get_years":"SELECT DISTINCT DATENAME({Year_Month},{column}) AS YEARS FROM {table}",
        "get_months":"SELECT DISTINCT DATENAME({Year_Month},{column}) AS MONTHS FROM {table}"
    }
    return QueryTemplate.get(command)

def GetTable(TableName):
    """Get The Table Name"""

    Tables={
        "data":"TbExpenseRecord"
    }
    return Tables.get(TableName)

def PopulateHome():
    """Populate the Home Page with Year, Month and Expense Type"""
    data = {}
    data.update(GetYears())
    data.update(GetMonths())
    data.update(GetAllData())
    return data

def GetYears():
    """ GET THE YEARS FOR WHICH DATA IS AVAILABLE """

    finalquery = GetQuery('get_years').format(Year_Month = 'YEAR', column = '[Date]', table=GetTable('data'))
    return GetRecords_FromDB(finalquery)

def GetMonths():
    """ GET THE MONTHS FOR WHICH DATA IS AVAILABLE """

    finalquery = GetQuery('get_months').format(Year_Month = 'MONTH', column = '[Date]', table=GetTable('data'))
    return GetRecords_FromDB(finalquery)

def GetAllData():
    """ GET THE MONTHS FOR WHICH DATA IS AVAILABLE """

    finalquery = GetQuery('select_all').format(columns = '*', table=GetTable('data'))
    df = pa.read_sql_query(finalquery,con=CreateConnection(), index_col = None)
    return df.to_dict(orient='split')

def DeriveQuery(parameterdict):
    """Form The Query"""
    
    finalquery = GetQuery('select').format(columns = '*', table=GetTable('data'))
    i = 0
    for k in parameterdict:
        if parameterdict.get(k) is not None and i == 0:
            finalquery = finalquery + '{} = \'{}\''.format(k,parameterdict.get(k))
            i+=1
        elif parameterdict.get(k) is not None and i > 0:
            finalquery = finalquery + ' and {} = \'{}\''.format(k,parameterdict.get(k))
            i+=1
    return GetRecords_FromDB(finalquery)

def GetRecords_FromDB(query):
    """Fetch Records From DB"""
        
    df = pa.read_sql_query(query,con=CreateConnection(), index_col = None)
    return df.to_dict()
