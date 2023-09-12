select distinct num as ConsecutiveNums
from (select num, lead(num, 1) over (order by id) as next, lead(num, 2) over(order by id) as afternext from logs) as l
where num = next and num = afternext
