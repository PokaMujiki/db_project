select polls_customer.name as customer_name,
       max(items.amount) as product_amount
from polls_receipt
inner join (
    select *
    from polls_receiptitem
    where polls_receiptitem.product_id = 4) as items
on polls_receipt.id = items.receipt_id
inner join polls_customer
on polls_customer.id = polls_receipt.customer_id
where items.amount >= 1
group by (polls_customer.id, polls_customer.name)