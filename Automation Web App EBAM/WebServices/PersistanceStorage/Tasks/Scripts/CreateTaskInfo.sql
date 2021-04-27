CREATE TABLE IF NOT EXISTS TaskInfo(
    TaskId INTEGER PRIMARY KEY,
    TaskTypeId INTEGER,
    TaskOnlyOnce INTEGER ,
    TaskInterval INTEGER,
    Description VARCHAR,
    TaskData VARCHAR,
    TaskLastRunTime VARCHAR,
    TaskLastRunSuccessfully INTEGER DEFAULT 0,
    IsDeleted DEFAULT 0,
    FOREIGN KEY (TaskTypeId) REFERENCES TaskType(TaskTypeId)
)