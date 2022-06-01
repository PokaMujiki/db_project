select polls_employee.name as employee_name,
       polls_tradepoint.name as point_name,
       polls_employee.salary as employee_salary
from polls_employee
inner join polls_tradepoint
on polls_tradepoint.point_type_id = 4
       and polls_employee.working_point_id = polls_tradepoint.id
order by polls_employee.salary desc