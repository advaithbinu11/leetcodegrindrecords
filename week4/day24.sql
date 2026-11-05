-- Write your PostgreSQL query statement below
with t1 as(
    SELECT recordDate AS rd, temperature AS otemp
    FROM Weather
)
SELECT id as Id
FROM Weather 
LEFT JOIN t1 ON t1.rd + INTERVAL '24 HOURS' = recordDate
WHERE otemp < temperature
-- Write your PostgreSQL query statement below
SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
WHERE transaction_id is null
GROUP BY customer_id
-- Write your PostgreSQL query statement below
SELECT product_name, year, price
FROM Sales AS s
LEFT JOIN Product AS p ON s.product_id = p.product_id
-- Write your PostgreSQL query statement below
SELECT unique_id, name
FROM Employees AS e
LEFT JOIN EmployeeUNI ON e.id = EmployeeUNI.id
-- Write your PostgreSQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15
-- Write your PostgreSQL query statement below
SELECT DISTINCT(author_id) AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id

-- Write your PostgreSQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000 or population >= 25000000

-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2 or referee_id is null

-- Write your PostgreSQL query statement below
SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'
