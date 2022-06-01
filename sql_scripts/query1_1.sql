select polls_distributor.name as distributor_name
from polls_distributor inner join polls_distributorproduct
on polls_distributorproduct.distributor_id = polls_distributor.id
where polls_distributorproduct.product_id = 1
group by polls_distributor.id