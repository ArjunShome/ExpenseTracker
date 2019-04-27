
def GetQuery(command):
    """Gives the Query template to the user for the required db command."""

    QueryTemplate = {
        "update":"UPDATE {table} SET {column} = {value} WHERE {condition}",
        "delete":"DELETE FROM {table} WHERE {condition}"
    }
    return QueryTemplate.get(command)


def GetQueryRecords(QyeryType):
    """Get Type Of SELECT Queries"""

    SelectQueryTemplate = {
        "fetchAll":"SELECT * FROM {TableName}",
        "fetch_WithCondition":"SELECT * FROM {TableName} WHERE {ColumnName} = {Value}"
    }
    return SelectQueryTemplate.get(QyeryType)

def GetTable(TableName):
    """Get The Table Name"""

    Tables={
        "data":"TbExpenseRecord"
    }
    return Tables.get(TableName)
