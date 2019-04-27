
def GetQuery(command):
    """Gives the Query template to the user for the required db command."""

    QueryTemplate = {
        "insert":"INSERT INTO {table} VALUES {data}",
        "update":"UPDATE {table} SET {column} = {value} WHERE {condition}",
        "delete":"DELETE FROM {table} WHERE {condition}"
    }
    return QueryTemplate[command]
