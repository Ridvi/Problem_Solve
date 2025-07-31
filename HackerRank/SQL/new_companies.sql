SELECT c.company_code,c.founder,
        count(distinct e.lead_manager_code),
        count(distinct e.senior_manager_code),
        count(distinct e.manager_code),
        count(distinct e.employee_code)
        
FROM company as c
join employee as e 
using(company_code)
group by c.company_code,c.founder
order by company_code;
