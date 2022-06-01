select polls_product.name as product_name,
       items.in_stock as in_stock,
       items.price as product_price
from (select *
        from polls_soldproduct
        where polls_soldproduct.trade_point_id = 1) as items
inner join polls_product
on polls_product.id = items.product_id