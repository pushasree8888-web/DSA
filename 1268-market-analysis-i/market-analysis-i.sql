# Write your MySQL query statement below
select u.user_id as buyer_id, u.join_date, count(o.buyer_id) as orders_in_2019
from users u left join orders o 
on user_id = buyer_id #and o.order_date >= '2019-01-01' and o.order_date < '2020-01-01'
and year(order_date) = "2019" 
group by user_id 
