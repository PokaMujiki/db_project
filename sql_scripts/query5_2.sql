select trade_points.name as trade_point_name,
       cast(sum(polls_receiptitem.price * polls_receiptitem.amount) as float4) / trade_points.employees_amount as profit
from polls_receiptitem
inner join (select *
            from polls_receipt
            where polls_receipt.date >= '2010-10-10' and polls_receipt.date <= '2022-12-12') as receipts
on polls_receiptitem.receipt_id = receipts.id
inner join (select polls_tradepoint.id as id,
                   polls_tradepoint.name as name,
                   polls_tradepoint.point_type_id as point_type,
                   count(*) as employees_amount
            from polls_tradepoint
            inner join polls_employee
            on polls_tradepoint.id = polls_employee.working_point_id
            group by (polls_tradepoint.id, polls_tradepoint.name)) as trade_points
on trade_points.point_type = 4 and receipts.trade_point_id = trade_points.id
group by (trade_points.id, trade_points.name, trade_points.employees_amount)
order by trade_points.name asc