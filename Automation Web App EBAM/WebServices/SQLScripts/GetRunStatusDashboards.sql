SELECT DISTINCT
       d.ID
     , d.Caption
     , d.IsInGroup
     , st.BadgeName
     , st.BadgeId
     , g.[Name] AS GroupName
     , d.IsPublic
     , cont.DisplayName AS Contact
     , cont.Email AS ContactEmail
     , creat.DisplayName AS Creator
     , creat.Email AS CreatorEmail
FROM [cockpit].Dashboards d
     LEFT OUTER JOIN [cockpit].[Group] g ON g.ID = d.GroupID
     LEFT OUTER JOIN [cockpit].DashboardBadges st ON st.BadgeId = d.BadgeId
     LEFT OUTER JOIN [cockpit].DashboardVersion dv ON dv.DashboardId = d.ID
                                                      AND dv.[Description] = st.BadgeName
     LEFT OUTER JOIN [ref].[User] cont ON cont.UserId = d.ContactPersonUserId
     INNER JOIN [ref].[User] creat ON creat.UserId = d.CreatedBy
     LEFT OUTER JOIN [ref].[User] u ON u.UserId = dv.CreatedBy
	 where st.BadgeName='run' and g.[Name] not like '%Personal%';