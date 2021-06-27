
-[X] An Sql query which returns columns with date, daily, weekly(rolling 7 day window) and monthly(rolling 30 day window) trading users for the last 30 days from current day.
     
    ```select date(execution_time) as date, 
    
    sum(day(execution_time)) over (
        partition by  extract(week from execution_time)
        order by day(execution_time)
    ) as Weekly_Users,
    sum(day(execution_time)) over (
        partition by extract(day from execution_time)
        order by day(execution_time)
    ) as Daily_Users,
        sum(day(execution_time)) over (
        partition by extract(month from execution_time)
        order by day(execution_time)
    ) as Monthly_Users
from trades
group by date(execution_time); ```
