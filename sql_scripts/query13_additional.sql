select polls_customer.name as customer_name,
       sum(polls_receiptitem.amount) as product_amount,
       sum(polls_receiptitem.price) as product_price
from polls_receiptitem
inner join (select *
            from polls_product
            where polls_product.id = 2) as product
on polls_receiptitem.product_id = product.id
inner join polls_receipt
on polls_receiptitem.receipt_id = polls_receipt.id
       and polls_receipt.date >= '2010-01-01'
       and polls_receipt.date <= '2022-12-12'
inner join polls_customer
on polls_customer.id = polls_receipt.customer_id
group by (polls_customer.id, polls_customer.name, product.id, polls_receiptitem.amount, polls_receiptitem.price)
