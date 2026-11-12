with t1 as (
    SELECT e.managerId, COUNT(e.managerId) as cnt
    FROM Employee as e
    GROUP BY e.managerId
)
SELECT name
FROM t1
JOIN Employee as sec ON t1.managerId = sec.id 
WHERE cnt >= 5
