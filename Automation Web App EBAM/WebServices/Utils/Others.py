def ReturnColumnEntryDict(DataSourceName, DataSource, TableName , ColumnName):
    Result = {}
    Result["DataSourceName"] = DataSourceName
    Result["DataSource"] = DataSource
    Result["TableName"] = TableName
    Result["ColumnName"] = ColumnName
    return Result
