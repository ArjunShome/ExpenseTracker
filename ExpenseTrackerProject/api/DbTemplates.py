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
        "select":"SELECT {columns} FROM {table} WHERE "
    }
    return QueryTemplate.get(command)

def GetTable(TableName):
    """Get The Table Name"""

    Tables={
        "data":"TbExpenseRecord"
    }
    return Tables.get(TableName)

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
    return finalquery

def GetRecords_FromDB(parameter):
        """Fetch Records From DB"""
        
        query = DeriveQuery(parameter)
        df = pa.read_sql_query(query,con=CreateConnection(), index_col = None)
        return df.to_dict()
