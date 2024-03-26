-- Lists the max temp of each state ordered by the stste name
-- source temperatures.sql;
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
