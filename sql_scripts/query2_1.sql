select polls_customer.name as customer_name from
polls_receipt
inner join (
    select *
    from polls_receiptitem
    where polls_receiptitem.product_id = 4) as items
on polls_receipt.id = items.receipt_id and polls_receipt.date >= '2010-01-01' and polls_receipt.date <= '2022-12-12'
inner join polls_customer
on polls_customer.id = polls_receipt.customer_id
group by (polls_customer.id, polls_customer.name)