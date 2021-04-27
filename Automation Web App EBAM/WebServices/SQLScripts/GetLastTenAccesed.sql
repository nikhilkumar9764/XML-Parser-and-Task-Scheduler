select Top 10  cockpit.Access.UserID as 'UserId',
             MAX(DisplayName) as 'UserName'
from
cockpit.access inner join
ref.[User]
on
cockpit.Access.UserId = ref.[User].UserId
where
DashboardID = ?
group by cockpit.Access.UserId
 order by MAX(DisplayDate) desc;
