path = 'WebServices/Config/DataBaseConnection.json'
CONFIG_FILE = "WebServices/Config/SQLScripts.json"
import json
class DatabaseActivities():

    def __init__(self):
        try:
            file = open(path)
            self.database_names = json.load(file)
            file.close()
            self.server = self.database_names["eBAMServer"]
            database = self.database_names['CustomizableCockpit']
            self.connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
            self.cursor = self.connection.cursor()
            self.Queries = {}
            SQLQueries = json.load(open(CONFIG_FILE))
            for query in SQLQueries:
                self.Queries[query] = open(SQLQueries[query]).read()
            self.test_db_connection()  # for testing connection
            print(self.Queries)
            self.get_query_execution_time(1,2)

        except Exception as e:
            print("Error In Connection : " + str(e))

    def test_db_connection(self):
        self.cursor.execute(self.Queries["DashboardXML"], 0)
        xml_string = self.cursor.fetchone()[0]
        print("\n DB Working Fine\n")


    def get_dashboard_xml(self, dashboard_id: int):
        self.cursor.execute(self.Queries["DashboardXML"], dashboard_id)
        xml_string = self.cursor.fetchone()[0]
        return xml_string

a = DatabaseActivities()