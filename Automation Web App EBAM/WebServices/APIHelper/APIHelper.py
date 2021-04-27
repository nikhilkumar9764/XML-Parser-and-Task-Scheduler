import requests
from WebServices.requests_negotiate_sspi import HttpNegotiateAuth
import json
from urllib.parse import quote
from requests import get

class APIHelper:

    @staticmethod
    def getDashboardInfo(DashboardId :int):
        URL = 'https://ebam-dashboard.eu.airbus.corp/2A24/Cockpit/Home/GetDashboardCardById?dashboardId='
        URL = URL + str(DashboardId)
        resp = get(URL, auth=HttpNegotiateAuth(), verify=False)
        return resp.json()

    @staticmethod
    def getDashboardJSON(DashboardId : int):
        headers = {'Content-Type': 'application/json'}
        URL_O = r"https://ebam-dashboard.eu.airbus.corp/2A24/Cockpit/dashboardDesigner/dashboards//" + str(DashboardId)

        DashboardJson = requests.get(url=URL_O, headers=headers, auth=HttpNegotiateAuth(), verify=False).json()
        return DashboardJson

    @staticmethod
    def getSQLQuery(Querypayload):
        URL_T = "https://ebam-dashboard.eu.airbus.corp/2A24/Cockpit/dashboardDesigner/data/DataSourceWizardAction/"
        FinalPayload = {}
        FinalPayload["actionKey"] = "getSelectStatement"
        FinalPayload["arg"] = quote(json.dumps(Querypayload).encode("utf-8"), safe="()'")
        Resp = requests.post(url=URL_T, json=FinalPayload, auth=HttpNegotiateAuth(), verify=False).json()
        return Resp

    @staticmethod
    def RenderDashboard(DashboardId, TimeOut , URL):
        URL_T = 'http://localhost:3000/testDashboard'
        FinalPayload = {}
        FinalPayload['dashboardId'] = str(DashboardId)
        FinalPayload['TimeOut'] = str(TimeOut)
        FinalPayload['URL'] = URL
        Response = requests.post(url=URL_T, json=FinalPayload).json()
        return Response





