from xml.etree import ElementTree
from WebServices.Dashboard.DashboardXML.DataSource import SQLDataSource

from WebServices.DataBaseUtils import DatabaseActivities

class DashBoardXMLHelper:

    @staticmethod
    def getXMLRoot(DashboardId : int):
        DashboardXML = DatabaseActivities.getInstance().getDashboardXML(DashboardId)
        xroot = ElementTree.fromstring(DashboardXML)
        return xroot

    @staticmethod
    def getIndexColumns(DashboardId :int):
        xroot = DashBoardXMLHelper.getXMLRoot(DashboardId)
        return DashBoardXMLHelper.ExtractColumnsFromXML(xroot)

    @staticmethod
    def isCoreAllDataSource(DataSource):
        DataSourceName = DataSource.find("Connection").attrib['Name']
        if "Core" in DataSourceName:
            return True
        return False

    @staticmethod
    def ExtractColumnsFromXML(xroot):
        Result = []
        for datasources in xroot.findall("DataSources"):
            for sqldatasrc in datasources.findall("SqlDataSource"):
                if not SQLDataSource.isCustomQuery(sqldatasrc):
                    Result = Result + SQLDataSource.ProcessSQLDataSource(sqldatasrc)
        return Result

    @staticmethod
    def getDataSourceInfo(DashboardId :int):
        xroot = DashBoardXMLHelper.getXMLRoot(DashboardId)
        result = {}
        for datasources in xroot.findall("DataSources"):
            for sqldatasrc in datasources.findall("SqlDataSource"):
                if SQLDataSource.getConnectionName(sqldatasrc) not in result:
                    result[SQLDataSource.getConnectionName(sqldatasrc)] = set([])
                result[SQLDataSource.getConnectionName(sqldatasrc)].update(SQLDataSource.getTables(sqldatasrc))
        for key in result:
            result[key] = list(result[key])
        return result

    @staticmethod
    def getCustomQueries(DashboardId :int):
        xroot = DashBoardXMLHelper.getXMLRoot(DashboardId)
        result = {}
        for datasources in xroot.findall("DataSources"):
            for sqldatasrc in datasources.findall("SqlDataSource"):
                if SQLDataSource.getConnectionName(sqldatasrc) not in result:
                    result[SQLDataSource.getConnectionName(sqldatasrc)] = []
                result[SQLDataSource.getConnectionName(sqldatasrc)].extend(SQLDataSource.getCustomQueries(sqldatasrc))
                if len(result[SQLDataSource.getConnectionName(sqldatasrc)]) == 0:
                    result.pop(SQLDataSource.getConnectionName(sqldatasrc), None)
        return result