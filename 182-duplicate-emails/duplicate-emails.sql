# Write your MySQL query statement below
# OWN SOLVED
select distinct a.email as Email 
from Person a 
cross join Person b 
where  a.id!=b.id 
and  a.email = b.email;