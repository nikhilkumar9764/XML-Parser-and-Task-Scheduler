import traceback
from WebServices.DataBaseUtils import *
from flask import request
import json
from WebServices.Dashboard.Dashboard import DashBoard
from WebServices.TaskSheduler.TaskScheduler import TaskScheduler
from WebServices.Task.TaskFactory import TaskFactory
from WebServices.PersistanceStorage.PersistanceStorage import PersistanceStorage


class Controller:
    __instance = None

    @staticmethod
    def getInstance():
        if Controller.__instance is None:
            Controller()
        return Controller.__instance

    def __init__(self):
        if Controller.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Controller.__instance = self
            self.DataBaseHandler = DatabaseActivities.getInstance()
            self.TaskScheduler = TaskScheduler.getInstance()
            self.PersistanceStorage = PersistanceStorage.getInstance()
            self.TaskFactory = TaskFactory()
            self.TaskScheduler.start()

    def getLastTenAccessed(self):
        try:
            dashboard_id = int(request.args.get('dashboardId'))
            print('LastTenAccessed ' + str(dashboard_id))
            return json.dumps(DashBoard.getLastTenAcessed(dashboard_id))
        except Exception as e:
            traceback.print_exc()
            return json.dumps({"Error": "Error "})

    def getDashboardInfo(self):
        try:
            dashboard_id = request.args.get('dashboardId')
            print(dashboard_id)
            resp = DashBoard.getDashboardInfo(dashboard_id)
            return resp
        except Exception as e:
            traceback.print_exc()
            print('Exception')
            return json.dumps({"Error": "Dashboard Id Incorrect" + str(e)})

    def getDataSourceInfo(self):
        try:
            dashboard_id = int(request.args.get('dashboardId'))
            response = json.dumps(DashBoard.getDataSourceInfo(dashboard_id))
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error": "Error In  Dashboard "+str(e)}

    def getCustomQueries(self):
        try:
            dashboard_id = request.args.get('dashboardId')
            response = json.dumps(DashBoard.getCustomQueries(dashboard_id))
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error": "Error In  Dashboard "+str(e)}

    def getAllQueries(self):
        try:
            dashboard_id = request.args.get('dashboardId')
            response = DashBoard.getAllSQLQueries(dashboard_id)
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error": "Error In  Dashboard "+str(e)}

    def getIndexes(self):
        try:
            dashboard_id = request.args.get('dashboardId')
            print('Here ' + str(dashboard_id))
            response = json.dumps(DashBoard.getIndexes(dashboard_id))
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error": "Error In  Dashboard "+str(e)}

    '''
        Later
    '''
    def getCustomQueryExecTime(self):
        print('getCustomQueryExecTime')
        return 1

    '''
            Later
    '''
    def getIndexSQLScript(self):
        print('getIndexSQLScript')
        return 1


    def getTaskDetails(self):
        print('GET TASK DETAILS')
        try:
            data = request.json
            TaskId = int(data["TaskId"])
            response = json.dumps(self.PersistanceStorage.Tasks.getTaskInfo(TaskId))
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error" : "Error Processing Request" + str(e)}

    def addNewTask(self):
        print('ADD A NEW TASK')
        try:
            data = request.json
            print(data)
            TaskType = data["TaskType"]
            Value = dict(data["Arg"])
            print(Value)
            Value["TaskId"] = self.PersistanceStorage.Tasks.getTaskId()
            NewTask = self.TaskFactory.getTask(TaskType, Value)
            NewTask.addTaskToStorage()
            self.TaskScheduler.addTask(NewTask)
            return {"TaskId" : Value["TaskId"]}
        except Exception as e:
            traceback.print_exc()
            return {"Error": str(e)}


    #Not To Be Done Now
    def UpdateTask(self):
        print('Update Task')

    def DeleteTask(self):
        print('Delete Task')
        try:
            data = request.json
            TaskId = int(data["TaskId"])
            if self.TaskScheduler.isTaskIdPresent(TaskId):
                response = {"Success" : self.TaskScheduler.deleteTaskById(TaskId)}
            else:
                response = {"Success" : self.PersistanceStorage.Tasks.deleteTaskById(TaskId)}
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error" : "Error Processing Request" + str(e)}

    def getAllTasks(self):
        print("Get All Tasks")
        try:
            response = json.dumps(self.PersistanceStorage.Tasks.getAllTasks())
            return response
        except Exception as e:
            traceback.print_exc()
            return {"Error" : "Error Processing Request" + str(e)}

    def getTasksStatus(self):
        print('Update Task')


    def __del__(self):
        print("end")
