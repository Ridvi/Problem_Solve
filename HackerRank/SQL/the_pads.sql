SELECT CONCAT(Name,"(",SUBSTRING(Occupation,1,1),")") AS name
FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT("There are a total of ",COUNT(Occupation)," ",LOWER(Occupation),"s.") AS number
FROM OCCUPATIONS 
GROUP BY Occupation
ORDER BY COUNT(Occupation),Occupation;
