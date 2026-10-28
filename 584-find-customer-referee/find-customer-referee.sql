-- Write your PostgreSQL query statement below
-- select name from Customer
-- where referee_id IS null or referee_id <> 2;

select name from Customer
where referee_id IS DISTINCT FROM 2;