select polls_customer.name as customer_name,
       sum(polls_receiptitem.price * polls_receiptitem.amount) as spent,
       sum(polls_receiptitem.amount) as product_amount
from polls_receiptitem
inner join (select *
            from polls_product
            where polls_product.id = 2) as product
on polls_receiptitem.product_id = product.id
inner join polls_receipt
on polls_receiptitem.receipt_id = polls_receipt.id
inner join polls_tradepoint
on polls_tradepoint.point_type_id = 1
       and polls_tradepoint.id = polls_receipt.trade_point_id
inner join polls_customer
on polls_customer.id = polls_receipt.customer_id
group by (polls_customer.id, polls_customer.name, product.id)
