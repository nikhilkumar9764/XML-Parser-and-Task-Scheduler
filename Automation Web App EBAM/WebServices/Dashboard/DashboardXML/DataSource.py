from xml.etree import ElementTree
from WebServices.Utils.Others import ReturnColumnEntryDict


class SQLDataSource:

    @staticmethod
    def isCustomQuery(SqlDataSource):
        QueryName = SqlDataSource.find("Query").attrib["Type"]
        if QueryName == "CustomSqlQuery":
            return True
        return False

    @staticmethod
    def ParseRelationTag(DataSourceName, DataSource, RelationTagRoot, TableList):
        Result = []
        ParentTable = TableList[RelationTagRoot.attrib['Parent']]
        ChildTable = TableList[RelationTagRoot.attrib['Nested']]

        for keycol in RelationTagRoot.findall('KeyColumn'):
            ParentCol = keycol.attrib['Parent']
            ChildCol = keycol.attrib['Nested']
            Result.append(ReturnColumnEntryDict(DataSourceName, DataSource, ParentTable, ParentCol))
            Result.append(ReturnColumnEntryDict(DataSourceName, DataSource, ChildTable, ChildCol))

        return Result

    @staticmethod
    def ParseFilterTag(DataSourceName, DataSource, FilterTagRoot):
        FilterTagText = FilterTagRoot.text
        startChar = '['
        endChar = ']'
        Result = []
        Flag = False
        ColumnName_ = ""
        for c in FilterTagText:
            if c == endChar:
                Flag = False
                TableName, ColumnName = ColumnName_.rsplit('.', 1)
                Result.append(ReturnColumnEntryDict(DataSourceName, DataSource, TableName, ColumnName))
                ColumnName_ = ""
            if Flag == True:
                ColumnName_ = ColumnName_ + c
            if c == startChar:
                Flag = True

        return Result

    @staticmethod
    def CreateTableDict(SqlDataSource):
        TableDict = {}
        for query in SqlDataSource.findall("Query"):
            if query.attrib['Type'] == "SelectQuery":
                for tables in query.findall("Tables"):

                    for table in tables.findall('Table'):

                        table_name = table.attrib['Name']
                        table_key = table_name

                        if 'Alias' in table.attrib:
                            table_key = table.attrib['Alias']
                        TableDict[table_key] = table_name

        return TableDict

    @staticmethod
    def ProcessSQLDataSource(sqldatasrc):
        Result = []
        TableList = SQLDataSource.CreateTableDict(sqldatasrc)
        DataSourceName, DataSource = SQLDataSource.getDatSourceDetails(sqldatasrc)

        for query in sqldatasrc.findall("Query"):
            for tables in query.findall("Tables"):
                for relation in tables.findall("Relation"):
                    Result = Result + SQLDataSource.ParseRelationTag(DataSourceName, DataSource, relation,
                                                                          TableList)
            for filter in query.findall("Filter"):
                Result = Result + SQLDataSource.ParseFilterTag(DataSourceName, DataSource, filter)

        return Result

    @staticmethod
    def getDatSourceDetails(DataSource):
        DataSourceName = DataSource.attrib['Name']
        DataSource = DataSource.find("Connection").attrib['Name']
        return DataSourceName, DataSource

    @staticmethod
    def getConnectionName(SQLDataSource):
        return SQLDataSource.find("Connection").attrib['Name']

    @staticmethod
    def getTables(SQLDataSource):
        result = set([])
        for query in SQLDataSource.findall("Query"):
            if query.attrib['Type'] == "SelectQuery":
                for tables in query.findall("Tables"):
                    for table in tables.findall('Table'):
                        table_name = table.attrib['Name']
                        result.add(table_name)
            elif query.attrib["Type"] == "CustomSqlQuery":
                result.add("Custom Query : "+str(query.attrib["Name"]))
            else:
                result.add(query.attrib["Type"] + " : " + str(query.findall("ProcName")[0].text))

        return result

    @staticmethod
    def getCustomQueries(SQLDataSource):
        result = list()
        for query in SQLDataSource.findall("Query"):
            if query.attrib["Type"] == "CustomSqlQuery":
                for sql in query.findall("Sql"):
                    result.append(sql.text)
        return list(result)



