select D.name Department, E.name Employee, E.salary Salary
from Employee E
inner join Department D on E.departmentId = D.id
where (E.departmentId, E.salary) in (select departmentId, max(salary)
                                    from Employee
                                    group by departmentId)

