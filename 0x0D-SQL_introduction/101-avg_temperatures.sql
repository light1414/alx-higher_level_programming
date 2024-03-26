-- It imports database dump temperatures.sql to database hbtn_0c_0 
-- then defines average temp by city ordered by temp (desc)
-- source temperatures.sql;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
