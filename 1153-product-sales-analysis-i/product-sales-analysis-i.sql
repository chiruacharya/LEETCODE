# Write your MySQL query statement below

# COMPLETELY OWN SOLVED

SELECT product_name ,year  ,price FROM Sales S INNER JOIN Product P ON S.product_id = P.product_id WHERE S.sale_id IS NOT NULL;