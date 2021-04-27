CREATE TABLE IF NOT EXISTS TaskResult(
    TaskId INTEGER,
    TaskResponse VARCHAR,
    TaskRunTime VARCHAR,
    FOREIGN KEY (TaskId) REFERENCES TaskInfo(TaskId)
)