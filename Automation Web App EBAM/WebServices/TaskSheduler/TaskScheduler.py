import threading
from queue import Queue
from WebServices.Task.Task import Task
from WebServices.PersistanceStorage.PersistanceStorage import PersistanceStorage

import time

class TaskScheduler(threading.Thread):
    __instance = None
    TaskQueue = Queue()
    TaskInfo = {}

    @staticmethod
    def getInstance():
        if TaskScheduler.__instance is None:
            TaskScheduler()
        return TaskScheduler.__instance

    def __init__(self):
        if TaskScheduler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            TaskScheduler.__instance = self
            super().__init__()

    def run(self):
        while True:
            if TaskScheduler.TaskQueue.empty():
                time.sleep(30)
            else :
                TaskToExecute = TaskScheduler.TaskQueue.get()
                if not TaskToExecute.isDeleted():
                    if TaskToExecute.ShouldRun(time.time()):
                        TaskToExecute.Init()
                        TaskToExecute.Run()
                    if TaskToExecute.isError() or not TaskToExecute.isOnlyOnce() :
                        TaskScheduler.TaskQueue.put(TaskToExecute)
                else:
                    TaskScheduler.TaskInfo.pop(TaskToExecute.getTaskId(), None)
                TaskToExecute.CleanUp()
                time.sleep(5)

    def addTask(self, NewTask):
        TaskScheduler.TaskQueue.put(NewTask)
        TaskScheduler.TaskInfo[NewTask.getTaskId()] = NewTask
        return NewTask.getTaskId()

    def deleteTaskById(self , TaskId):
        if TaskId not in TaskScheduler.TaskInfo:
            raise Exception("No Such Tasks")
        TaskScheduler.TaskInfo[TaskId].setIsDeleted()
        return "Task SuccessFully Deleted In TaskQueue"

    def isTaskIdPresent(self, TaskId):
        if TaskId not in TaskScheduler.TaskInfo:
            return False
        return True

    def updateTask(self):
        raise Exception('Update Task Not Implemented')





