select polls_product.name as name,
       polls_productorderitem.price as price,
       polls_productorderitem.amount as amount
from polls_productorderitem
inner join (select *
            from polls_productsorder
            where polls_productsorder.id = 1) as product_order
on polls_productorderitem.products_order_id = product_order.id
inner join polls_distributorproduct
on polls_productorderitem.distributor_product_id = polls_distributorproduct.id
inner join polls_product
on polls_distributorproduct.product_id = polls_product.id