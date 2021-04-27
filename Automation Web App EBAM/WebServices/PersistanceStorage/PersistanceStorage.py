from WebServices.PersistanceStorage.Tasks.Tasks import Tasks


class PersistanceStorage:
    __instance = None

    @staticmethod
    def getInstance():
        if PersistanceStorage.__instance is None:
            PersistanceStorage()
        return PersistanceStorage.__instance

    def __init__(self):
        if PersistanceStorage.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PersistanceStorage.__instance = self
            self.Tasks = Tasks.getInstance()







