select trade_point_expenses.name as point_name,
       cast(sum(polls_receiptitem.amount * polls_receiptitem.price) as float4) / trade_point_expenses.expenses as profitability
from polls_receipt
inner join (select polls_tradepoint.name as name,
                   polls_tradepoint.id as point_id,
                   sum(polls_employee.salary) + coalesce(polls_tradepoint.utilities_payment, 0) + coalesce(polls_tradepoint.rent_payment, 0) as expenses
            from polls_tradepoint
            inner join polls_employee
            on polls_tradepoint.id = polls_employee.working_point_id
            group by (polls_tradepoint.id, polls_tradepoint.name, polls_tradepoint.utilities_payment, polls_tradepoint.rent_payment)) as trade_point_expenses
on polls_receipt.trade_point_id = trade_point_expenses.point_id
inner join polls_receiptitem
on polls_receipt.id = polls_receiptitem.receipt_id
group by (trade_point_expenses.point_id, trade_point_expenses.name, trade_point_expenses.expenses)
order by profitability desc

