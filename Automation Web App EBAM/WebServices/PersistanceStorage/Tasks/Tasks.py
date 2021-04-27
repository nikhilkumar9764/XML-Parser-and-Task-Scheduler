import sqlite3
import json

DB_LOCATION = 'DynamicData/TaskData.db'
SQL_SCRIPTS_ON_INIT = 'WebServices/PersistanceStorage/Tasks/TasksSQLScriptsOnLoad.json'

class Tasks:
    __instance = None

    @staticmethod
    def getInstance():
        if Tasks.__instance is None:
            Tasks()
        return Tasks.__instance

    def __init__(self):
        if Tasks.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Tasks.__instance = self
            self.conn = sqlite3.connect(DB_LOCATION, check_same_thread=False)
            self.cur = self.conn.cursor()
            self.InitiliazeDBTable()
            self.LoadTaskTypes()

    def InitiliazeDBTable(self):
        SciptsOnInit = json.load(open(SQL_SCRIPTS_ON_INIT))
        print(SciptsOnInit)
        for key in SciptsOnInit:
            print(key)
            self.cur.execute(open(SciptsOnInit[key]).read())
        self.conn.commit()

    def getTaskId(self):
        TaskId = 1
        SQL = "SELECT * FROM TaskInfo"
        response = self.cur.execute(SQL).fetchall()
        print(response)
        if len(response) > 0 :
            TaskId = len(response) + 1
        return TaskId

    def getAllTasks(self):
        SQL = "SELECT TaskId, TaskName, Description, TaskOnlyOnce,TaskInterval,TaskData, TaskLastRunTime, TaskLastRunSuccessfully " \
              "FROM TaskInfo INNER JOIN TaskType ON TaskInfo.TaskTypeId=TaskType.TaskTypeId WHERE IsDeleted=0 "
        TaskList = self.cur.execute(SQL).fetchall()
        Rows = ["TaskId", "TaskName", "Description", "TaskOnlyOnce", "TaskInterval", "TaskData", "TaskLastRunTime",
                "TaskLastRunSuccessfully"]
        Response = []
        print(TaskList)
        for row in TaskList:
            TaskInfo = dict()
            Index = 0
            for rowName in Rows:
                if rowName == "TaskData":
                    TaskInfo[rowName] = dict(json.loads(row[Index]))
                else:
                    TaskInfo[rowName] = row[Index]
                Index = Index + 1
            Response.append(TaskInfo)
        return Response

    def getTaskInfo(self, TaskId: int):
        SQL = "SELECT TaskId,TaskResponse, TaskRunTime FROM TaskResult WHERE TaskId = ? LIMIT 5"
        Tasks = self.cur.execute(SQL, [TaskId]).fetchall()
        Lables = ["TaskId", "TaskResult", "TaskLastRunTime"]
        Response = []
        for task in Tasks:
            cnt = 0
            Task = {}
            for label in Lables:
                if label == "TaskResult":
                    Task[label] = dict(json.loads(task[cnt]))
                else:
                    Task[label] = task[cnt]
                cnt = cnt + 1
            Response.append(Task)
        return Response

    def checkTaskType(self, TaskTypeId):
        SQL = "SELECT * FROM TaskType WHERE TaskTypeId = ?"
        self.cur.execute(SQL, [TaskTypeId])
        if len(self.cur.fetchall()) > 0:
            return True
        return False

    def addTask(self, TaskId:int , TaskTypeId:int, TaskOnlyOnce:int, TaskInterval:int, Description:str, TaskData:str, TaskLastRunTime:str):
        Input = [TaskId, TaskTypeId, TaskOnlyOnce, TaskInterval, Description, TaskData, TaskLastRunTime]
        print('Input List ' , Input)
        SQL = "Insert Into TaskInfo (TaskId , TaskTypeId, TaskOnlyOnce, TaskInterval, Description, TaskData" \
              " , TaskLastRunTime) Values (? , ? , ? , ? , ? , ? , ?) "
        self.cur.execute(SQL , Input)
        self.conn.commit()
        return "Task Added SuccessFully"

    def updateExistingTaskStatus(self, TaskId , TaskLastRunTime:str, TaskLastRunSuccessfully:int):
        SQL = "UPDATE TaskInfo SET TaskLastRunTime = ? , TaskLastRunSuccessfully = ? WHERE TaskId = ? "
        self.cur.execute(SQL, [TaskLastRunTime, TaskLastRunSuccessfully, TaskId])
        self.conn.commit()
        return "SuccessFully Updated Task"


    def addTaskType(self, TaskTypeId:int, TaskName:str, TaskDescription:str):
        Input = [TaskTypeId, TaskName, TaskDescription]
        print(Input)
        self.cur.execute("Insert into TaskType(TaskTypeId, TaskName, TaskDescription) Values(?, ?, ?)", Input)
        self.conn.commit()

    def addTaskResult(self, TaskId:int, TaskResult:str, TaskRunTime:str):
        Input = [TaskId, TaskResult, TaskRunTime]
        self.cur.execute("Insert into TaskResult(TaskId, TaskResponse , TaskRunTime) Values(?, ?, ?)", Input)
        self.conn.commit()

    def LoadTaskTypes(self):
        self.cur.execute("Select * from TaskType")
        resp = self.cur.fetchall()
        print(resp)

    def deleteTaskById(self, TaskId: int):
        SQL = "UPDATE TaskInfo SET IsDeleted=1 WHERE TaskId= ?"
        self.cur.execute(SQL, [TaskId])
        self.conn.commit()
        return "SuccessFully DELETED FROM Storage"

