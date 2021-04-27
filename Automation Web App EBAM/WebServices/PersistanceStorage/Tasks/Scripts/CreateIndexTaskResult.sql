CREATE UNIQUE INDEX IF NOT EXISTS IDX_TASK_RESULT
 ON TaskResult
   (
      TaskId ,
      TaskRunTime
   )