from WebServices.Task.Task import Task
from WebServices.APIHelper.APIHelper import APIHelper
import time


class DashboardTest(Task):

    def Init(self):
        self.Error = False

    def Run(self):
        print('Dashboard Task Run', self.TaskData["DashboardId"], self.TaskData["TimeOut"])
        Response = APIHelper.RenderDashboard(self.TaskData["DashboardId"], self.TaskData["TimeOut"],
                                             self.TaskData["DashboarUrl"])
        self.Output = Response
        self.LastRunTime = time.time()
        self.CheckForError()
        self.saveResultToStorage()
        self.updateExistingTaskStatus()

    def CheckForError(self):
        if self.Output is None:
            self.Error = 0
        elif "Error" in self.Output:
            self.Error = -1
        else:
            self.Error = 1


    def CleanUp(self):
        self.Output = None
        self.Error = False

    def __init__(self, TaskId:int, TaskInterval:int, OnlyOnce:int, Description:str, Value:dict):
        super().__init__(TaskId=TaskId, TaskTypeId=1, TaskInterval=TaskInterval, OnlyOnce=OnlyOnce,
                         Description=Description)
        if TaskId is None:
            raise Exception("TaskId Not Provided")
        if "DashboardId" not in Value:
            raise Exception("DashboardId Not Provided")
        if "DashboardUrl" not in Value:
            raise Exception("DashboardUrl Not Provided")
        if "TimeOut" not in Value:
            raise Exception("Timeout Not Provided")
        self.TaskData = dict()
        self.TaskData["DashboarUrl"] = Value["DashboardUrl"]
        self.TaskData["DashboardId"] = Value["DashboardId"]
        self.TaskData["TimeOut"] = Value["TimeOut"]

