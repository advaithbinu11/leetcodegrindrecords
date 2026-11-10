# Write your MySQL query statement below
SELECT act.machine_id, ROUND(AVG(bact.timestamp - act.timestamp), 3) as processing_time
FROM Activity AS act
JOIN Activity AS bact ON act.machine_id = bact.machine_id AND act.process_id = bact.process_id AND act.activity_type != bact.activity_type 
WHERE act.activity_type = 'start'
GROUP BY act.machine_id 
