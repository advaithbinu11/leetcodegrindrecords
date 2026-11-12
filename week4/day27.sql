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
