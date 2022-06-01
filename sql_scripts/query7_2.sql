select polls_tradepoint.name as point_name,
       sum(polls_receiptitem.amount * polls_receiptitem.price) as profit
from polls_receiptitem
inner join (select *
            from polls_product
            where polls_product.id = 2) as product
on polls_receiptitem.product_id = product.id
inner join polls_receipt
on polls_receiptitem.receipt_id = polls_receipt.id
       and polls_receipt.date >= '2010-01-01'
       and polls_receipt.date <= '2022-12-12'
inner join polls_tradepoint
on polls_tradepoint.point_type_id = 4
       and polls_receipt.trade_point_id = polls_tradepoint.id
group by (polls_tradepoint.id, polls_tradepoint.name)
