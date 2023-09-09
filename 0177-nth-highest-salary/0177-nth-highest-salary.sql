CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    select case when count(sub.salary) < N then NULL else min(sub.salary) end
    from (select distinct salary
            from employee
            order by salary desc
            limit N) as sub
  );
END