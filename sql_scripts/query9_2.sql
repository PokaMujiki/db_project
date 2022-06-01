select orders.date as date,
       polls_productorderitem.price as price,
       polls_productorderitem.amount as amount
from polls_productorderitem
inner join (select *
            from polls_productsorder
            where polls_productsorder.date >= '2010-01-01' and polls_productsorder.date <= '2022-12-12') as orders
on polls_productorderitem.products_order_id = orders.id
inner join polls_distributorproduct
on polls_distributorproduct.distributor_id = 19
       and polls_productorderitem.distributor_product_id = polls_distributorproduct.id
       and polls_distributorproduct.product_id = 4
