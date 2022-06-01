select polls_customer.name as customer_name,
       sum(polls_receiptitem.amount * polls_receiptitem.price) as spent
from polls_customer
inner join polls_receipt
on polls_customer.id = polls_receipt.customer_id
inner join polls_receiptitem
on polls_receipt.id = polls_receiptitem.receipt_id
inner join polls_tradepoint
on polls_receipt.trade_point_id = polls_tradepoint.id
       and polls_tradepoint.point_type_id = 1
group by (polls_customer.id, polls_customer.name)
order by spent desc