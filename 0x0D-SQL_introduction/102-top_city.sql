-- Display top 3 of cities temperature during July an August
SELECT `city`m AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 or `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
