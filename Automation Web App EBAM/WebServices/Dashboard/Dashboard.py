from xml.etree import ElementTree
from WebServices.Dashboard.DashboardXML.DataSource import SQLDataSource
from WebServices.DataBaseUtils import DatabaseActivities
from WebServices.Dashboard.DashboardXML.DashboardXML import DashBoardXMLHelper
from WebServices.APIHelper.APIHelper import APIHelper
from WebServices.Dashboard.DashboardJSON.DashboardJSON import DashBoardJSONHelper
import json


class DashBoard:

    @staticmethod
    def getDashboardInfo(DashboardId : int):
        return APIHelper.getDashboardInfo(DashboardId)

    @staticmethod
    def getLastTenAcessed(DashboardId:int):
        return DatabaseActivities.getInstance().LastTenAccesed(DashboardId)


    @staticmethod
    def getDataSourceInfo(DashboardId : int):
        return DashBoardXMLHelper.getDataSourceInfo(DashboardId)


    @staticmethod
    def getCustomQueries(DashboardId : int):
        return DashBoardXMLHelper.getCustomQueries(DashboardId)

    @staticmethod
    def getIndexes(DashboardId : int):
        return list(DashBoardXMLHelper.getIndexColumns(DashboardId))

    @staticmethod
    def getAllSQLQueries(DashboardId : int):
        return DashBoardJSONHelper.GetSQLQueriesOfDashboard(DashboardId)