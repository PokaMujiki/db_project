select employee.name as name,
       sum(polls_receiptitem.price * polls_receiptitem.amount) as profit
from polls_tradepoint
inner join (select *
            from polls_employee
            where polls_employee.id = 1) as employee
on polls_tradepoint.id = 1
inner join polls_receipt
on polls_tradepoint.id = polls_receipt.trade_point_id
       and polls_receipt.employee_id = employee.id
       and polls_receipt.date >= '2010-01-01'
       and polls_receipt.date <= '2022-12-12'
inner join polls_receiptitem
on polls_receipt.id = polls_receiptitem.receipt_id
group by (employee.id, employee.name)
