select polls_productsorder.date as date,
       polls_productorderitem.price as price,
       polls_productorderitem.amount as amount
from polls_productorderitem
inner join polls_productsorder
on polls_productorderitem.products_order_id = polls_productsorder.id
inner join polls_distributorproduct
on polls_distributorproduct.distributor_id = 19
       and polls_productorderitem.distributor_product_id = polls_distributorproduct.id
       and polls_distributorproduct.product_id = 4
