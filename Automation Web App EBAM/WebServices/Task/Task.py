from abc import abstractmethod, ABC
import time
from WebServices.PersistanceStorage.PersistanceStorage import PersistanceStorage
import json

class Task(ABC):

    def __init__(self, TaskId, TaskTypeId, OnlyOnce=False , TaskInterval=36000, Description="Not Given" ):
        self.isInitialized = True
        self.LastRunTime = time.time()
        self.OnlyOnce = OnlyOnce
        self.IsDeleted = False
        self.Output = None
        self.TaskInterVal = TaskInterval
        self.TaskData = None
        self.Error = 0
        self.TaskTypeId = TaskTypeId
        self.Description = Description
        self.TaskId = TaskId

    def getTaskData(self):
        return self.TaskData

    def setTaskData(self, TaskData):
        self.TaskData = TaskData

    def setLastRunTime(self , LastRunTime):
        self.LastRunTime = LastRunTime

    def isOnlyOnce(self):
        return self.OnlyOnce

    def isDeleted(self):
        return self.IsDeleted

    def setIsDeleted(self):
        self.IsDeleted = True
        self.removeTaskFromStorage()

    def getTaskTypeId(self):
        return self.TaskTypeId

    def getTaskId(self):
        return self.TaskId

    def ShouldRun(self, CurrentTime):
        if self.OnlyOnce :
            return True
        if (CurrentTime - self.LastRunTime) > self.TaskInterVal:
            return True
        return False

    def addTaskToStorage(self):
        if not self.isInitialized:
            raise Exception("Task Not Initiliased")
        PersistanceStorage.getInstance().Tasks.addTask(self.TaskId, self.TaskTypeId, int(self.OnlyOnce), self.TaskInterVal, self.Description, json.dumps(self.TaskData), str(self.LastRunTime))
        return "Success"

    def updateExistingTaskStatus(self):
        PersistanceStorage.getInstance().Tasks.updateExistingTaskStatus(self.TaskId, str(self.LastRunTime), self.Error)

    def saveResultToStorage(self):
        PersistanceStorage.getInstance().Tasks.addTaskResult(self.TaskId, json.dumps(self.Output), str(time.time()))
        return "Success"

    def removeTaskFromStorage(self):
        PersistanceStorage.getInstance().Tasks.deleteTaskById(self.TaskId)
        return "Success"

    def isError(self):
        return self.Error

    @abstractmethod
    def Init(self):
        raise NotImplementedError

    @abstractmethod
    def CleanUp(self):
        raise NotImplementedError

    @abstractmethod
    def CheckForError(self):
        raise NotImplementedError

    @abstractmethod
    def Run(self):
        raise NotImplementedError
