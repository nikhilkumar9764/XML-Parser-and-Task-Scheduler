from xml.etree import ElementTree


class SQLDataSource:

    def __init__(self, sqldatasource):

        self.SqlDataSource = sqldatasource
        self.column_set = set([])
        self.custom_query_list = []
        self.table_list = dict()
        self.connection_name = sqldatasource.find("Connection").attrib['Name']
        self.process()

    def getConnectionName(self):
        return self.connection_name

    def getTables(self):
        result = set([])
        for query in self.SqlDataSource.findall("Query"):
            if query.attrib['Type'] == "SelectQuery":
                for tables in query.findall("Tables"):
                    for table in tables.findall('Table'):
                        table_name = table.attrib['Name']
                        result.add(table_name)
            elif query.attrib["Type"] == "CustomSqlQuery":
                result.add("Custom Query")

        return list(result)

    def getCustomQueries(self):
        result = list()
        for query in self.SqlDataSource.findall("Query"):
            if query.attrib["Type"] == "CustomSqlQuery":
                for sql in query.findall("Sql"):
                    result.append(sql.text)
        return list(result)

    def getAllColumns(self):
        return self.column_set


    def addDatasourceInfo(self , sql):
        sql = "/* \n  Connection Name :" + self.connection_name + "\n */ \n\n" + sql + "\n"
        return sql


    def getAllQueries(self):
        return self.custom_query_list

    def parse_relation_tag(self, relation):

        parent = self.table_list[relation.attrib['Parent']]
        child = self.table_list[relation.attrib['Nested']]

        for keycol in relation.findall('KeyColumn'):
            parent_col = keycol.attrib['Parent']
            child_col = keycol.attrib['Nested']
            self.column_set.add((self.connection_name , str(parent) + "." + str(parent_col)))
            self.column_set.add((self.connection_name, str(child) + "." + str(child_col)))

    def parse_filter_tag(self, filter):

        filter_text = str(filter.text)
        filter_col = ""
        flag = False
        for c in filter_text:

            if c == ']':
                flag = False
                self.column_set.add((self.connection_name , filter_col))
                filter_col = ""
            if flag:
                filter_col = filter_col + c

            if c == '[':
                flag = True

    def process(self):
        for query in self.SqlDataSource.findall("Query"):
            if query.attrib['Type'] == "SelectQuery":
                for tables in query.findall("Tables"):

                    for table in tables.findall('Table'):

                        table_name = table.attrib['Name']
                        table_key = table_name

                        if 'Alias' in table.attrib:
                            table_key = table.attrib['Alias']

                       # if table_name.endswith("View"):
                        #    table_name = table_name[:-4]

                        self.table_list[table_key] = table_name

                    for relation in tables.findall("Relation"):
                        self.parse_relation_tag(relation)
                for filter in query.findall("Filter"):
                    self.parse_filter_tag(filter)
            elif query.attrib["Type"] == "CustomSqlQuery":
                for sql in query.findall("Sql"):
                    self.custom_query_list.append(self.addDatasourceInfo(sql.text))

