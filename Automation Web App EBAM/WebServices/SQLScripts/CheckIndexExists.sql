SELECT  TOP 1 ColumnsCount = COUNT(*)
    FROM    sys.index_columns AS ic
            INNER JOIN sys.indexes AS i
                ON ic.[object_id] = i.[object_id]
                AND ic.index_id = i.index_id
            INNER JOIN sys.columns AS c
                ON ic.[object_id] = c.[object_id]
                AND ic.column_id = c.column_id
    WHERE   ic.[object_id] = OBJECT_ID(?)
    AND     i.[type] != 0
    AND     ic.is_included_column = 0
    GROUP BY i.index_id
    HAVING  COUNT(CASE WHEN c.Name = ? THEN 1 END) > 0
    ORDER BY ColumnsCount;