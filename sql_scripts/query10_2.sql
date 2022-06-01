select trade_points_halls_amount.point_name as point_name,
       cast(sum(polls_receiptitem.price * polls_receiptitem.amount) as float4) / trade_points_halls_amount.halls_amount as profit_div
from polls_receipt
inner join (select polls_tradepoint.id as id,
                   polls_tradepoint.name as point_name,
                   count(polls_tradepoint.id) as halls_amount
            from polls_tradepoint
            inner join polls_hall
            on polls_tradepoint.point_type_id = 2
                   and polls_tradepoint.id = polls_hall.trade_point_id
            group by (polls_tradepoint.id, polls_tradepoint.name)) as trade_points_halls_amount
on polls_receipt.trade_point_id = trade_points_halls_amount.id
inner join polls_receiptitem
on polls_receipt.id = polls_receiptitem.receipt_id
group by (trade_points_halls_amount.id, trade_points_halls_amount.point_name, trade_points_halls_amount.halls_amount)
order by profit_div desc
