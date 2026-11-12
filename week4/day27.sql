with t1 as (
    SELECT e.managerId, COUNT(e.managerId) as cnt
    FROM Employee as e
    GROUP BY e.managerId
)
SELECT name
FROM t1
JOIN Employee as sec ON t1.managerId = sec.id 
WHERE cnt >= 5
#better version
SELECT e2.name
FROM Employee as e1
JOIN Employee as e2 ON e1.managerId = e2.id
GROUP BY e1.managerId
HAVING COUNT(*) >= 5
SELECT *
FROM Cinema
WHERE id % 2 = 1 AND description != "boring"
ORDER BY rating DESC
# Write your MySQL query statement below
with t1 AS (
    SELECT product_id, SUM(units) as total
    FROM UnitsSold as u
    GROUP BY product_id
), t2 AS (
    SELECT p.product_id, price * units as rev
    FROM Prices AS p
    JOIN UnitsSold as u ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND end_date
)
SELECT t2.product_id, ROUND(SUM(rev) / total, 2) as average_price
FROM t2
JOIN t1 ON t1.product_id = t2.product_id
GROUP BY t1.product_id
