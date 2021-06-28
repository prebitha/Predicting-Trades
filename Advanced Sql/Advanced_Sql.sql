# 1.  An Sql query which returns columns with date, daily, weekly(rolling 7 day window) 
# and monthly(rolling 30 day window) trading users for the last 30 days from current day.

select date(execution_time) as date, 
    sum(count(customer_id)) over (
        partition by extract(week from execution_time)
        order by date(execution_time)
    ) as Weekly_Users,
    sum(count(customer_id)) over (
        partition by extract(day from execution_time)
        order by date(execution_time)
    ) as Daily_Users,
        sum(count(customer_id)) over (
        partition by extract(month from execution_time)
        order by date(execution_time)
    ) as Monthly_Users
from trades
group by date(execution_time);

#-------------------------------------------------------------------------------------------------------------------------------------

# 2. An query to indicate trading volume for each day ( sum of all trade total of that day).

SELECT date(execution_time) as date , customer_id as user, direction, count(execution_size) as total 
from trades
group by date(execution_time);

#-------------------------------------------------------------------------------------------------------------------------------------

# 3. A query that will return set of 30 rows for further anaylsis.


SELECT date(execution_time) as date , customer_id as user, direction, count(execution_size) as total 
from trades
group by date(execution_time)
limit 30;

