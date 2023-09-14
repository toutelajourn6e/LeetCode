select E1.name as Employee
from employee E1, employee E2
where E1.managerid = E2.id and E1.salary > E2.salary