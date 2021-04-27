import json
import pyodbc
import datetime


path = 'WebServices/Config/DataBaseConnection.json'
CONFIG_FILE = "WebServices/Config/SQLScripts.json"

class DatabaseActivities:
    __instance = None

    def __init__(self):
        if DatabaseActivities.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseActivities.__instance = self
        try:
            file = open(path)
            self.database_names = json.load(file)
            file.close()
            self.server = self.database_names["eBAMServer"]
            database = self.database_names['CustomizableCockpit']
            self.connection = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
            self.cursor = self.connection.cursor()
            self.Queries = {}
            SQLQueries = json.load(open(CONFIG_FILE))
            for query in SQLQueries:
                self.Queries[query] = open(SQLQueries[query]).read()
            self.test_db_connection()  # for testing connection
            #self.get_query_execution_time(1,2)

        except Exception as e:
            print("Error In Connection : " + str(e))

    @staticmethod
    def getInstance():
        if DatabaseActivities.__instance is None:
            DatabaseActivities()
        return DatabaseActivities.__instance

    def test_db_connection(self):
        self.cursor.execute(self.Queries["DashboardXML"], 0)
        xml_string = self.cursor.fetchone()[0]
        print("\n DB Working Fine\n")


    def getDashboardXML(self, dashboard_id: int):
        self.cursor.execute(self.Queries["DashboardXML"], dashboard_id)
        xml_string = self.cursor.fetchone()[0]
        return xml_string

    def get_query_execution_time(self , sql_query, datasource):

        '''
        init_time = datetime.datetime.now()

        cursor.execute(sql_query)

        end_time = datetime.datetime.now()
        exec_time = end_time - init_time

        print('exec_time  = {} seconds '.format(exec_time.seconds))
        '''

        strr = json.load(open('WebServices/Config/DBConnection.json'))
        print(strr)
        temp = list(strr)
        print(temp)
        xyz = {}
        for db in temp:
            print(db)
            print(dict(db))
            xyz[dict(db)['name']] = dict(db)

        print(xyz)
        print('here in query execution time')
        return 1

    def CheckIndexOnColumn(self,ColumnName , DataSource):
        print('here check Indexes')
        return True

    def GetRunStatusDashboards(self):
        print('here')
        return 1

    def GetDashboardInfo(self , dashboard_id : int):
        print(dashboard_id)
        return 1

    def LastTenAccesed(self,dashboard_id:int):
        self.cursor.execute(self.Queries["LastTenAccesed"], dashboard_id)
        return dict(self.cursor.fetchall())



    def __del__(self):
        self.cursor.close()
        self.connection.close()


