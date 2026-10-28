-- -- Write your PostgreSQL query statement below
-- select e.employee_id
-- from Employees e
-- LEFT JOIN Employees m
--     ON e.manager_id = m.employee_id
-- where e.salary < 30000
--     and e.manager_id is not null
--     and m.employee_id is null
-- order by e.employee_id;

select employee_id
from Employees
where salary < 30000 
    and manager_id is not null 
    and manager_id not in (select employee_id from Employees)
order by employee_id;