select T.dn as Department, T.n as Employee, T.s as Salary
from(
    select D.name as dn, E.name as n, E.salary as s, dense_rank() over (partition by D.id order by E.salary desc) as r
    from Employee E
        inner join Department D on E.departmentId = D.id) as T
where T.r <= 3