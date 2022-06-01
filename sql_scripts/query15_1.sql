select polls_product.name as product_name,
       polls_tradepoint.name as trade_point_name,
       polls_soldproduct.in_stock as in_stock,
       polls_soldproduct.price as price
from polls_soldproduct
inner join polls_tradepoint
on polls_soldproduct.trade_point_id = polls_tradepoint.id
       and polls_tradepoint.point_type_id = 1
inner join polls_product
on polls_soldproduct.product_id = polls_product.id
order by (polls_product.name, polls_tradepoint.name) asc
