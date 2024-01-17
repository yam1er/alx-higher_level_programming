-- write a script that lists all recorsds with score >= 10 in th table
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
