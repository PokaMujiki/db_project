select polls_tradepoint.name as point_name,
       sum(polls_receiptitem.price * polls_receiptitem.amount) / polls_tradepoint.point_counter_amount as profit_div_counter_amount
from polls_receipt
inner join polls_tradepoint
on polls_tradepoint.point_type_id = 1
       and polls_receipt.trade_point_id = polls_tradepoint.id
inner join polls_receiptitem
on polls_receipt.id = polls_receiptitem.receipt_id
where polls_tradepoint.point_counter_amount is not null
group by (polls_tradepoint.id, polls_tradepoint.name, polls_tradepoint.point_counter_amount)
order by profit_div_counter_amount desc