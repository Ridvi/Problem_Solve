SELECT CONCAT(MAX(months*salary)," ",COUNT(*)) AS result
FROM EMPLOYEE
GROUP BY months*salary
ORDER BY months*salary DESC
LIMIT 1;
