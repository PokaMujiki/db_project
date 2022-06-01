select polls_tradepoint.name as trade_point_name,
       items.price as price,
       items.in_stock as in_stock
from (select *
      from polls_soldproduct
      where polls_soldproduct.product_id = 2) as items
inner join polls_tradepoint
on items.trade_point_id = polls_tradepoint.id