# Write your MySQL query statement below
SELECT name, bonus
FROM Employee as e
left Join Bonus as b on e.empid = b.empid
where bonus < 1000 or bonus is null
