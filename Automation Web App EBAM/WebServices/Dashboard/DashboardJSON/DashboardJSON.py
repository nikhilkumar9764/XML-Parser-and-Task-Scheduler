import json
from WebServices.APIHelper.APIHelper import APIHelper


class DashBoardJSONHelper:

    @staticmethod
    def ExtractDataSources(DashboardJSON):
        DataSources = DashboardJSON["Dashboard"]['DataSources']
        DataSourcesList = []
        for key, value in DataSources.items():
            DataSourcesList.append(value)
        return DataSourcesList


    @staticmethod
    def GetSQLQueriesOfDashboard(DashboardId: int):
        Result = {}
        DashboardJSON = APIHelper.getDashboardJSON(DashboardId)
        DataSources = DashBoardJSONHelper.ExtractDataSources(DashboardJSON)
        for DataSource in DataSources:
            Result[DashBoardJSONHelper.GetDataSourceName(DataSource)] = DashBoardJSONHelper.GetDataSourceQuery(DataSource)
        return Result


    @staticmethod
    def GenerateDataSourceJson(DataSource):
        DataSourceJSON = {}
        connectionJSON = {}
        connectionJSON['DataConnection'] = DataSource['Connection']
        connectionJSON['ConnectionOptions'] = DataSource['ConnectionOptions']

        sqlQueryJSON = {}
        sqlQueryJSON['Query'] = DataSource['Queries']['Item1']
        DataSourceJSON['connectionJSON'] = json.dumps(connectionJSON)
        DataSourceJSON['sqlQueryJSON'] = json.dumps(sqlQueryJSON)
        return DataSourceJSON


    @staticmethod
    def getSQLQuery(Querypayload):
        Resp = APIHelper.getSQLQuery(Querypayload)
        return Resp['result']['sqlSelectStatement']


    @staticmethod
    def CheckCustomQuery(DataSource):
        if DataSource["Queries"]["Item1"]["@Type"] == "CustomSqlQuery":
            return True
        return False

    @staticmethod
    def CheckStoredProc(DataSource):
        if DataSource["Queries"]["Item1"]["@Type"] == "StoredProcQuery":
            return True
        return False


    @staticmethod
    def CheckSelectQuery(DataSource):
        if DataSource["Queries"]["Item1"]["@Type"] == "SelectQuery":
            return True
        return False


    @staticmethod
    def GetCustomQuery(DataSource):
        if DataSource["Queries"]["Item1"]["@Type"] == "StoredProcQuery":
            return DataSource["Queries"]["Item1"]["ProcName"]
        return DataSource["Queries"]["Item1"]["Sql"]


    @staticmethod
    def GetDataSourceName(DataSource):
        return str(DataSource["@Name"])


    @staticmethod
    def GetDataSourceQuery(DataSource):
        if DashBoardJSONHelper.CheckCustomQuery(DataSource):
            return DashBoardJSONHelper.GetCustomQuery(DataSource)
        DataSourceJSON = DashBoardJSONHelper.GenerateDataSourceJson(DataSource)
        SQLQuery = DashBoardJSONHelper.getSQLQuery(DataSourceJSON)
        return SQLQuery


