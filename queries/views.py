from django.db import connection
from django.shortcuts import render

from .forms import *


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def query1(request):
    if request.method != 'POST':
        return render(request, 'queries/query1.html', {'form': Query1Form(), 'data': None, 'error': None,
                                                       'complicated_view': None})
    data = None
    warning = None
    complicated_view = None
    form = Query1Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            required_product = form.cleaned_data.get("required_product").pk
            volume = form.cleaned_data.get("volume")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")

            if (start_date is None and end_date is not None) or (start_date is not None and end_date is None):
                warning = "Please, specify date correctly"
                return render(request, 'queries/query1.html', {'form': form, 'data': data, 'warning': warning,
                                                   'complicated_view': complicated_view})

            if volume is None:
                cursor.execute("select polls_distributor.name as distributor_name from polls_distributor "
                               "inner join polls_distributorproduct on "
                               "polls_distributorproduct.distributor_id = polls_distributor.id where "
                               "polls_distributorproduct.product_id = {0} group by "
                               "polls_distributor.id".format(required_product))
                data = dict_fetchall(cursor)
            elif start_date is not None and end_date is not None:
                if start_date > end_date:
                    warning = "Please, specify date correctly"
                    render(request, 'queries/query1.html', {'form': form, 'data': data, 'warning': warning,
                                                            'complicated_view': complicated_view})
                complicated_view = True
                cursor.execute("select * from (select polls_distributor.name as distributor_name,              "
                               "sum(distr_product.amount) as product_amount       from polls_distributor       inner "
                               "join (select *                   from polls_productorderitem                   inner "
                               "join polls_productsorder                   on "
                               "polls_productorderitem.products_order_id = polls_productsorder.id                     "
                               "  and polls_productsorder.date >= '{2}'                       and "
                               "polls_productsorder.date <= '{3}'                   inner join "
                               "polls_distributorproduct                   on "
                               "polls_productorderitem.distributor_product_id = polls_distributorproduct.id           "
                               "        where polls_distributorproduct.product_id = {0}) as distr_product       on "
                               "polls_distributor.id = distr_product.distributor_id       group by ("
                               "polls_distributor.id, polls_distributor.name)) as distr_product_amount where "
                               "distr_product_amount.product_amount >= {1}"
                               .format(required_product, volume, start_date, end_date))
                data = dict_fetchall(cursor)
            else:
                complicated_view = True
                cursor.execute("select * from (select polls_distributor.name as distributor_name,              "
                               "sum(distr_product.amount) as product_amount       from polls_distributor       inner "
                               "join (select *                   from polls_productorderitem                   inner "
                               "join polls_distributorproduct                   on "
                               "polls_productorderitem.distributor_product_id = polls_distributorproduct.id           "
                               "        where polls_distributorproduct.product_id = {0}) as distr_product       on "
                               "polls_distributor.id = distr_product.distributor_id       group by ("
                               "polls_distributor.id, polls_distributor.name)) as distr_product_amount where "
                               "distr_product_amount.product_amount >= {1} "
                               .format(required_product, volume))
                data = dict_fetchall(cursor)
    return render(request, 'queries/query1.html', {'form': form, 'data': data, 'warning': warning,
                                                   'complicated_view': complicated_view})


def query2(request):
    if request.method != 'POST':
        return render(request, 'queries/query2.html', {'form': Query2Form(), 'data': None, 'warning': None,
                                                       'complicated_view': None})
    data = None
    warning = None
    complicated_view = None
    form = Query2Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            required_product = form.cleaned_data.get("required_product").pk
            volume = form.cleaned_data.get("volume")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            if (start_date is None and end_date is not None) or (start_date is not None and end_date is None):
                warning = "Bad date input fields"
            else:
                if volume is not None:
                    if start_date is not None and end_date is not None:
                        warning = "Date is ignored in this query"
                    complicated_view = True
                    cursor.execute("select polls_customer.name as customer_name,         max(items.amount) as "
                                   "product_amount  from polls_receipt  inner join (      select *      from "
                                   "polls_receiptitem      where polls_receiptitem.product_id = {0}) as items  on "
                                   "polls_receipt.id = items.receipt_id  inner join polls_customer  on "
                                   "polls_customer.id = polls_receipt.customer_id  where items.amount >= {1}  group "
                                   "by (polls_customer.id, polls_customer.name) "
                                   .format(required_product, volume))
                    data = dict_fetchall(cursor)
                elif start_date is None or end_date is None or start_date > end_date:
                    warning = "Please, specify date correctly"
                else:
                    cursor.execute("select polls_customer.name as customer_name from polls_receipt inner join "
                                   "(     select *     from polls_receiptitem     where "
                                   "polls_receiptitem.product_id = 4) as items on polls_receipt.id = "
                                   "items.receipt_id and polls_receipt.date >= '2010-01-01' and "
                                   "polls_receipt.date <= '2022-12-12' inner join polls_customer on "
                                   "polls_customer.id = polls_receipt.customer_id group by ("
                                   "polls_customer.id, polls_customer.name) "
                                   .format(required_product, start_date, end_date))
                    data = dict_fetchall(cursor)
    return render(request, 'queries/query2.html', {'form': form, 'data': data, 'warning': warning,
                                                   'complicated_view': complicated_view})


def query3(request):
    if request.method != 'POST':
        return render(request, 'queries/query3.html', {'form': Query3Form(request.POST), 'data': None, 'warning': None})

    data = None
    warning = None
    form = Query3Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            trade_point = form.cleaned_data.get("trade_point").pk
            cursor.execute("select polls_product.name as product_name,        items.in_stock as in_stock,        "
                           "items.price as product_price from (select *         from polls_soldproduct         "
                           "where polls_soldproduct.trade_point_id = {0}) as items inner join polls_product on "
                           "polls_product.id = items.product_id"
                           .format(trade_point))
            data = dict_fetchall(cursor)
    return render(request, 'queries/query3.html', {'form': form, 'data': data, 'warning': warning})


def query4(request):
    if request.method != 'POST':
        return render(request, 'queries/query4.html', {'form': Query4Form(), 'data': None, 'warning': None})

    data = None
    warning = None
    form = Query4Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            product = form.cleaned_data.get("product").pk
            trade_point_type = None
            trade_point = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk
            if form.cleaned_data.get("trade_point") is not None:
                trade_point = form.cleaned_data.get("trade_point").pk
            if trade_point_type is None and trade_point is None:
                cursor.execute("select polls_tradepoint.name as trade_point_name,        items.price as price, "
                               "items.in_stock as in_stock from (select *       from polls_soldproduct      where "
                               "polls_soldproduct.product_id = {0}) as items inner join polls_tradepoint on "
                               "items.trade_point_id = polls_tradepoint.id "
                               .format(product))
            elif trade_point is None:
                cursor.execute("select polls_tradepoint.name as trade_point_name,        items.price as price,    "
                               "    items.in_stock as in_stock from (select *       from polls_soldproduct       "
                               "where polls_soldproduct.product_id = {0}) as items inner join polls_tradepoint on "
                               "items.trade_point_id = polls_tradepoint.id inner join polls_tradepointtype on "
                               "polls_tradepoint.point_type_id = {1} and polls_tradepoint.point_type_id = "
                               "polls_tradepointtype.id "
                               .format(product, trade_point_type))
            else:
                if trade_point_type is not None:
                    warning = "Trade point type is ignored because concrete trade point is specified"
                cursor.execute("select polls_tradepoint.name as trade_point_name,        items.price as price,    "
                               "    items.in_stock as in_stock from (select *       from polls_soldproduct       "
                               "where polls_soldproduct.product_id = {0}) as items inner join polls_tradepoint on "
                               "items.trade_point_id = polls_tradepoint.id and items.trade_point_id = {1} "
                               .format(product, trade_point))
            data = dict_fetchall(cursor)
    return render(request, 'queries/query4.html', {'form': form, 'data': data, 'warning': warning})


def query5(request):
    if request.method != 'POST':
        return render(request, 'queries/query5.html', {'form': Query5Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query5Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            trade_point_type = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk

            if start_date > end_date:
                warning = "Please, specify date correctly"
                return render(request, 'queries/query5.html', {'form': Query5Form(), 'data': data, 'warning': warning})

            if trade_point_type is None:
                cursor.execute("select trade_points.name as trade_point_name,         sum(polls_receiptitem.price * "
                               "polls_receiptitem.amount) / trade_points.employees_amount as profit  from "
                               "polls_receiptitem  inner join (select *              from polls_receipt              "
                               "where polls_receipt.date >= '{0}' and polls_receipt.date <= '{1}') as "
                               "receipts  on polls_receiptitem.receipt_id = receipts.id  inner join (select "
                               "polls_tradepoint.id as id,                     polls_tradepoint.name as name,         "
                               "            count(*) as employees_amount              from polls_tradepoint           "
                               "   inner join polls_employee              on polls_tradepoint.id = "
                               "polls_employee.working_point_id              group by (polls_tradepoint.id, "
                               "polls_tradepoint.name)) as trade_points  on receipts.trade_point_id = trade_points.id "
                               " group by (trade_points.id, trade_points.name, trade_points.employees_amount)  order "
                               "by trade_points.name asc  "
                               .format(start_date, end_date))
            else:
                cursor.execute("select trade_points.name as trade_point_name,         sum(polls_receiptitem.price * "
                               "polls_receiptitem.amount) / trade_points.employees_amount as profit  from "
                               "polls_receiptitem  inner join (select *              from polls_receipt              "
                               "where polls_receipt.date >= '{0}' and polls_receipt.date <= '{1}') as "
                               "receipts  on polls_receiptitem.receipt_id = receipts.id  inner join (select "
                               "polls_tradepoint.id as id,                     polls_tradepoint.name as name,         "
                               "            polls_tradepoint.point_type_id as point_type,                     "
                               "count(*) as employees_amount              from polls_tradepoint              inner "
                               "join polls_employee              on polls_tradepoint.id = "
                               "polls_employee.working_point_id              group by (polls_tradepoint.id, "
                               "polls_tradepoint.name)) as trade_points  on trade_points.point_type = {2} and "
                               "receipts.trade_point_id = trade_points.id  group by (trade_points.id, "
                               "trade_points.name, trade_points.employees_amount)  order by trade_points.name asc  "
                               .format(start_date, end_date, trade_point_type))

            data = dict_fetchall(cursor)
    return render(request, 'queries/query5.html', {'form': form, 'data': data, 'warning': warning})


def query6(request):
    if request.method != 'POST':
        return render(request, 'queries/query6.html', {'form': Query6Form(), 'data': None})
    data = None
    form = Query6Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            employee = form.cleaned_data.get("employee").pk
            trade_point = form.cleaned_data.get("trade_point").pk
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")

            if start_date > end_date:
                warning = "Please, specify date correctly"
                return render(request, 'queries/query6.html', {'form': Query6Form(), 'data': data, 'warning': warning})

            cursor.execute("select employee.name as name,        sum(polls_receiptitem.price * "
                           "polls_receiptitem.amount) as profit from polls_tradepoint inner join (select *            "
                           " from polls_employee             where polls_employee.id = {0}) as employee on "
                           "polls_tradepoint.id = {1} inner join polls_receipt on polls_tradepoint.id = "
                           "polls_receipt.trade_point_id         and polls_receipt.employee_id = employee.id         "
                           "and polls_receipt.date >= '{2}'         and polls_receipt.date <= '{3}' "
                           "inner join polls_receiptitem on polls_receipt.id = polls_receiptitem.receipt_id group by "
                           "(employee.id, employee.name) "
                           .format(employee, trade_point, start_date, end_date))

            data = dict_fetchall(cursor)
    return render(request, 'queries/query6.html', {'form': form, 'data': data})


def query7(request):
    if request.method != 'POST':
        return render(request, 'queries/query7.html', {'form': Query7Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query7Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            product = form.cleaned_data.get("product").pk
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            trade_point_type = None
            trade_point = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk
            if form.cleaned_data.get("trade_point") is not None:
                trade_point = form.cleaned_data.get("trade_point").pk

            if start_date > end_date:
                warning = "Please, specify date correctly"
                return render(request, 'queries/query7.html', {'form': Query7Form(), 'data': data, 'warning': warning})

            if trade_point_type is None and trade_point is None:
                cursor.execute("select polls_tradepoint.name as point_name,        sum(polls_receiptitem.amount * "
                               "polls_receiptitem.price) as profit from polls_receiptitem inner join (select *        "
                               "     from polls_product             where polls_product.id = {0}) as product on "
                               "polls_receiptitem.product_id = product.id inner join polls_receipt on "
                               "polls_receiptitem.receipt_id = polls_receipt.id        and polls_receipt.date >= "
                               "'{1}'        and polls_receipt.date <= '{2}' inner join "
                               "polls_tradepoint on polls_receipt.trade_point_id = polls_tradepoint.id group by ("
                               "polls_tradepoint.id, polls_tradepoint.name) "
                               .format(product, start_date, end_date))
            elif trade_point is not None:
                if trade_point_type is not None:
                    warning = "Trade point type is ignored because concrete trade point is specified"
                cursor.execute("select polls_tradepoint.name as point_name,        sum(polls_receiptitem.amount * "
                               "polls_receiptitem.price) as profit from polls_receiptitem inner join (select *        "
                               "     from polls_product             where polls_product.id = {0}) as product on "
                               "polls_receiptitem.product_id = product.id inner join polls_receipt on "
                               "polls_receiptitem.receipt_id = polls_receipt.id        and polls_receipt.date >= "
                               "'{1}'        and polls_receipt.date <= '{2}' inner join "
                               "polls_tradepoint on polls_tradepoint.id = {3}        and polls_receipt.trade_point_id = "
                               "polls_tradepoint.id group by (polls_tradepoint.id, polls_tradepoint.name) "
                               .format(product, start_date, end_date, trade_point))
            else:
                cursor.execute("select polls_tradepoint.name as point_name,        sum(polls_receiptitem.amount * "
                               "polls_receiptitem.price) as profit from polls_receiptitem inner join (select *        "
                               "     from polls_product             where polls_product.id = {0}) as product on "
                               "polls_receiptitem.product_id = product.id inner join polls_receipt on "
                               "polls_receiptitem.receipt_id = polls_receipt.id        and polls_receipt.date >= "
                               "'{1}'        and polls_receipt.date <= '{2}' inner join "
                               "polls_tradepoint on polls_tradepoint.point_type_id = {3}        and "
                               "polls_receipt.trade_point_id = polls_tradepoint.id group by (polls_tradepoint.id, "
                               "polls_tradepoint.name) "
                               .format(product, start_date, end_date, trade_point_type))

            data = dict_fetchall(cursor)
    return render(request, 'queries/query7.html', {'form': form, 'data': data, 'warning': warning})


def query8(request):
    if request.method != 'POST':
        return render(request, 'queries/query8.html', {'form': Query8Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query8Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            trade_point_type = None
            trade_point = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk
            if form.cleaned_data.get("trade_point") is not None:
                trade_point = form.cleaned_data.get("trade_point").pk

            if trade_point is not None:
                if trade_point_type is not None:
                    warning = "Trade point type is ignored because concrete trade point is specified"
                cursor.execute("select polls_employee.name as employee_name,        polls_tradepoint.name as "
                               "point_name,        polls_employee.salary as employee_salary from polls_employee inner "
                               "join polls_tradepoint on polls_tradepoint.id = {0}        and "
                               "polls_employee.working_point_id = polls_tradepoint.id order by polls_employee.salary "
                               "desc"
                               .format(trade_point))
            elif trade_point_type is not None:
                cursor.execute("select polls_employee.name as employee_name,        polls_tradepoint.name as "
                               "point_name,        polls_employee.salary as employee_salary from polls_employee inner "
                               "join polls_tradepoint on polls_tradepoint.point_type_id = {0}        and "
                               "polls_employee.working_point_id = polls_tradepoint.id order by polls_employee.salary "
                               "desc"
                               .format(trade_point_type))
            else:
                cursor.execute("select polls_employee.name as employee_name,        polls_tradepoint.name as "
                               "point_name,        polls_employee.salary as employee_salary from polls_employee inner "
                               "join polls_tradepoint on polls_employee.working_point_id = polls_tradepoint.id order "
                               "by polls_employee.salary desc")
            data = dict_fetchall(cursor)
    return render(request, 'queries/query8.html', {'form': form, 'data': data, 'warning': warning})


def query9(request):
    if request.method != 'POST':
        return render(request, 'queries/query9.html', {'form': Query9Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query9Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            product = form.cleaned_data.get("product").pk
            distributor = form.cleaned_data.get("distributor").pk
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")

            if start_date is None and end_date is None:
                cursor.execute("select polls_productsorder.date as date,         polls_productorderitem.price as "
                               "price,         polls_productorderitem.amount as amount  from polls_productorderitem  "
                               "inner join polls_productsorder  on polls_productorderitem.products_order_id = "
                               "polls_productsorder.id  inner join polls_distributorproduct  on "
                               "polls_distributorproduct.distributor_id = {0}         and "
                               "polls_productorderitem.distributor_product_id = polls_distributorproduct.id         "
                               "and polls_distributorproduct.product_id = {1}  "
                               .format(distributor, product))
                data = dict_fetchall(cursor)
            elif start_date is None or end_date is None or start_date > end_date:
                warning = "Please, specify date correctly"
            else:
                cursor.execute("select orders.date as date,          polls_productorderitem.price as price,          "
                               "polls_productorderitem.amount as amount   from polls_productorderitem   inner join ("
                               "select *               from polls_productsorder               where "
                               "polls_productsorder.date >= '{2}' and polls_productsorder.date <= "
                               "'{3}') as orders   on polls_productorderitem.products_order_id = orders.id   "
                               "inner join polls_distributorproduct   on polls_distributorproduct.distributor_id = {0} "
                               "         and polls_productorderitem.distributor_product_id = "
                               "polls_distributorproduct.id          and polls_distributorproduct.product_id = {1}   "
                               .format(distributor, product, start_date, end_date))
                data = dict_fetchall(cursor)
    return render(request, 'queries/query9.html', {'form': form, 'data': data, 'warning': warning})


def query10(request):
    if request.method != 'POST':
        return render(request, 'queries/query10.html', {'form': Query10Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query10Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            trade_point_type = form.cleaned_data.get("trade_point_type").pk
            my_filter = form.cleaned_data.get("filter")

            if my_filter == "Point size":
                cursor.execute("select polls_tradepoint.name as point_name,          cast(sum(polls_receiptitem.price "
                               "* polls_receiptitem.amount) as float4) / polls_tradepoint.point_size as profit_div   "
                               "from polls_receipt   inner join polls_tradepoint   on polls_tradepoint.point_type_id "
                               "= {0}          and polls_receipt.trade_point_id = polls_tradepoint.id   inner join "
                               "polls_receiptitem   on polls_receipt.id = polls_receiptitem.receipt_id   where "
                               "polls_tradepoint.point_size is not null   group by (polls_tradepoint.id, "
                               "polls_tradepoint.name, polls_tradepoint.point_size)   order by profit_div desc "
                               .format(trade_point_type))
                data = dict_fetchall(cursor)
            elif my_filter == "Halls amount":
                if trade_point_type != 1 and trade_point_type != 2:
                    warning = "Specified trade point type can't contain halls"
                else:
                    cursor.execute("select trade_points_halls_amount.point_name as point_name,          cast(sum("
                                   "polls_receiptitem.price * polls_receiptitem.amount) as float4) / "
                                   "trade_points_halls_amount.halls_amount as profit_div   from polls_receipt   inner "
                                   "join (select polls_tradepoint.id as id,                      "
                                   "polls_tradepoint.name as point_name,                      "
                                   "count(polls_tradepoint.id) as halls_amount               from polls_tradepoint    "
                                   "           inner join polls_hall               on polls_tradepoint.point_type_id "
                                   "= {0}                      and polls_tradepoint.id = polls_hall.trade_point_id     "
                                   "         group by (polls_tradepoint.id, polls_tradepoint.name)) as "
                                   "trade_points_halls_amount   on polls_receipt.trade_point_id = "
                                   "trade_points_halls_amount.id   inner join polls_receiptitem   on polls_receipt.id "
                                   "= polls_receiptitem.receipt_id   group by (trade_points_halls_amount.id, "
                                   "trade_points_halls_amount.point_name, trade_points_halls_amount.halls_amount)   "
                                   "order by profit_div desc "
                                   .format(trade_point_type))
                    data = dict_fetchall(cursor)
            elif my_filter == "Counters amount":
                cursor.execute("select polls_tradepoint.name as point_name,          cast(sum(polls_receiptitem.price "
                               "* polls_receiptitem.amount) as float4) / polls_tradepoint.point_counter_amount as "
                               "profit_div   from polls_receipt   inner join polls_tradepoint   on "
                               "polls_tradepoint.point_type_id = {0}          and polls_receipt.trade_point_id = "
                               "polls_tradepoint.id   inner join polls_receiptitem   on polls_receipt.id = "
                               "polls_receiptitem.receipt_id   where polls_tradepoint.point_counter_amount is not "
                               "null   group by (polls_tradepoint.id, polls_tradepoint.name, "
                               "polls_tradepoint.point_counter_amount)   order by profit_div desc "
                               .format(trade_point_type))
                data = dict_fetchall(cursor)
    return render(request, 'queries/query10.html', {'form': form, 'data': data, 'warning': warning})


def query11(request):
    with connection.cursor() as cursor:
        cursor.execute("select trade_point_expenses.name as point_name,          cast(sum(polls_receiptitem.amount * "
                       "polls_receiptitem.price) as float4) / trade_point_expenses.expenses as profitability   from "
                       "polls_receipt   inner join (select polls_tradepoint.name as name,                      "
                       "polls_tradepoint.id as point_id,                      sum(polls_employee.salary) + coalesce("
                       "polls_tradepoint.utilities_payment, 0) + coalesce(polls_tradepoint.rent_payment, "
                       "0) as expenses               from polls_tradepoint               inner join polls_employee    "
                       "           on polls_tradepoint.id = polls_employee.working_point_id               group by ("
                       "polls_tradepoint.id, polls_tradepoint.name, polls_tradepoint.utilities_payment, "
                       "polls_tradepoint.rent_payment)) as trade_point_expenses   on polls_receipt.trade_point_id = "
                       "trade_point_expenses.point_id   inner join polls_receiptitem   on polls_receipt.id = "
                       "polls_receiptitem.receipt_id   group by (trade_point_expenses.point_id, "
                       "trade_point_expenses.name, trade_point_expenses.expenses)   order by profitability desc      ")

        data = dict_fetchall(cursor)
    return render(request, 'queries/query11.html', {'data': data})


def query12(request):
    if request.method != 'POST':
        return render(request, 'queries/query12.html', {'form': Query12Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query12Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            product_order = form.cleaned_data.get("product_order").pk

            cursor.execute("select polls_product.name as name,          polls_productorderitem.price as price,        "
                           "  polls_productorderitem.amount as amount   from polls_productorderitem   inner join ("
                           "select *               from polls_productsorder               where "
                           "polls_productsorder.id = {0}) as product_order   on "
                           "polls_productorderitem.products_order_id = product_order.id   inner join "
                           "polls_distributorproduct   on polls_productorderitem.distributor_product_id = "
                           "polls_distributorproduct.id   inner join polls_product   on "
                           "polls_distributorproduct.product_id = polls_product.id"
                           .format(product_order))

            data = dict_fetchall(cursor)
    return render(request, 'queries/query12.html', {'form': form, 'data': data, 'warning': warning})


def query13(request):
    if request.method != 'POST':
        return render(request, 'queries/query13.html', {'form': Query13Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query13Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            product = form.cleaned_data.get("product").pk
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            trade_point_type = None
            trade_point = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk
            if form.cleaned_data.get("trade_point") is not None:
                trade_point = form.cleaned_data.get("trade_point").pk

            if start_date is None and end_date is None:
                if trade_point is not None:
                    if trade_point_type is not None:
                        warning = "Trade point type is ignored because concrete trade point is specified"
                    cursor.execute("select polls_customer.name as customer_name,          sum(polls_receiptitem.price "
                                   "* polls_receiptitem.amount) as spent,          sum(polls_receiptitem.amount) as "
                                   "product_amount   from polls_receiptitem   inner join (select *               from "
                                   "polls_product               where polls_product.id = {0}) as product   on "
                                   "polls_receiptitem.product_id = product.id   inner join polls_receipt   on "
                                   "polls_receiptitem.receipt_id = polls_receipt.id   inner join polls_tradepoint   "
                                   "on polls_tradepoint.id = {1}          and polls_tradepoint.id = "
                                   "polls_receipt.trade_point_id   inner join polls_customer   on polls_customer.id = "
                                   "polls_receipt.customer_id   group by (polls_customer.id, polls_customer.name, "
                                   "product.id)   "
                                   .format(product, trade_point))
                elif trade_point_type is not None:
                    cursor.execute("select polls_customer.name as customer_name,          sum(polls_receiptitem.price "
                                   "* polls_receiptitem.amount) as spent,          sum(polls_receiptitem.amount) as "
                                   "product_amount   from polls_receiptitem   inner join (select *               from "
                                   "polls_product               where polls_product.id = {0}) as product   on "
                                   "polls_receiptitem.product_id = product.id   inner join polls_receipt   on "
                                   "polls_receiptitem.receipt_id = polls_receipt.id   inner join polls_tradepoint   "
                                   "on polls_tradepoint.point_type_id = {1}          and polls_tradepoint.id = "
                                   "polls_receipt.trade_point_id   inner join polls_customer   on polls_customer.id = "
                                   "polls_receipt.customer_id   group by (polls_customer.id, polls_customer.name, "
                                   "product.id)   "
                                   .format(product, trade_point_type))
                else:
                    cursor.execute("select polls_customer.name as customer_name,          sum(polls_receiptitem.price "
                                   "* polls_receiptitem.amount) as spent,          sum(polls_receiptitem.amount) as "
                                   "product_amount   from polls_receiptitem   inner join (select *               from "
                                   "polls_product               where polls_product.id = {0}) as product   on "
                                   "polls_receiptitem.product_id = product.id   inner join polls_receipt   on "
                                   "polls_receiptitem.receipt_id = polls_receipt.id   inner join polls_customer   on "
                                   "polls_customer.id = polls_receipt.customer_id   group by (polls_customer.id, "
                                   "polls_customer.name, product.id)   "
                                   .format(product))
                data = dict_fetchall(cursor)
            elif start_date is None or end_date is None or start_date > end_date:
                warning = "Please, specify date correctly"
            elif trade_point is not None:
                if trade_point_type is not None:
                    warning = "Trade point type is ignored because concrete trade point is specified"
                cursor.execute("select polls_customer.name as customer_name,           sum(polls_receiptitem.price * "
                               "polls_receiptitem.amount) as spent,           sum(polls_receiptitem.amount) as "
                               "product_amount    from polls_receiptitem    inner join (select *                from "
                               "polls_product                where polls_product.id = {0}) as product    on "
                               "polls_receiptitem.product_id = product.id    inner join polls_receipt    on "
                               "polls_receiptitem.receipt_id = polls_receipt.id           and polls_receipt.date >= "
                               "'{2}'           and polls_receipt.date <= '{3}'    inner join "
                               "polls_tradepoint    on polls_tradepoint.id = {1}           and polls_tradepoint.id = "
                               "polls_receipt.trade_point_id    inner join polls_customer    on polls_customer.id = "
                               "polls_receipt.customer_id    group by (polls_customer.id, polls_customer.name, "
                               "product.id)    "
                               .format(product, trade_point, start_date, end_date))
                data = dict_fetchall(cursor)
            elif trade_point_type is not None:
                cursor.execute("select polls_customer.name as customer_name,           sum(polls_receiptitem.price * "
                               "polls_receiptitem.amount) as spent,           sum(polls_receiptitem.amount) as "
                               "product_amount    from polls_receiptitem    inner join (select *                from "
                               "polls_product                where polls_product.id = {0}) as product    on "
                               "polls_receiptitem.product_id = product.id    inner join polls_receipt    on "
                               "polls_receiptitem.receipt_id = polls_receipt.id           and polls_receipt.date >= "
                               "'{2}'           and polls_receipt.date <= '{3}'    inner join "
                               "polls_tradepoint    on polls_tradepoint.point_type_id = {1}           and "
                               "polls_tradepoint.id = polls_receipt.trade_point_id    inner join polls_customer    on "
                               "polls_customer.id = polls_receipt.customer_id    group by (polls_customer.id, "
                               "polls_customer.name, product.id)    "
                               .format(product, trade_point_type, start_date, end_date))
                data = dict_fetchall(cursor)
            else:
                cursor.execute("select polls_customer.name as customer_name,           sum(polls_receiptitem.price * "
                               "polls_receiptitem.amount) as spent,           sum(polls_receiptitem.amount) as "
                               "product_amount    from polls_receiptitem    inner join (select *                from "
                               "polls_product                where polls_product.id = {0}) as product    on "
                               "polls_receiptitem.product_id = product.id    inner join polls_receipt    on "
                               "polls_receiptitem.receipt_id = polls_receipt.id           and polls_receipt.date >= "
                               "'{1}'           and polls_receipt.date <= '{2}'    inner join "
                               "polls_customer    on polls_customer.id = polls_receipt.customer_id    group by ("
                               "polls_customer.id, polls_customer.name, product.id)    "
                               .format(product, start_date, end_date))
                data = dict_fetchall(cursor)
    return render(request, 'queries/query13.html', {'form': form, 'data': data, 'warning': warning})


def query14(request):
    if request.method != 'POST':
        return render(request, 'queries/query14.html', {'form': Query14Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query14Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            trade_point_type = None
            trade_point = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk
            if form.cleaned_data.get("trade_point") is not None:
                trade_point = form.cleaned_data.get("trade_point").pk

            if trade_point is not None:
                if trade_point_type is not None:
                    warning = "Trade point type is ignored because concrete trade point is specified"
                cursor.execute("select polls_customer.name as customer_name,          sum(polls_receiptitem.amount * "
                               "polls_receiptitem.price) as spent   from polls_customer   inner join polls_receipt   "
                               "on polls_customer.id = polls_receipt.customer_id   inner join polls_receiptitem   on "
                               "polls_receipt.id = polls_receiptitem.receipt_id   inner join polls_tradepoint   on "
                               "polls_receipt.trade_point_id = polls_tradepoint.id          and polls_tradepoint.id = "
                               "{0}   group by (polls_customer.id, polls_customer.name)   order by spent desc "
                               .format(trade_point))
            elif trade_point_type is not None:
                cursor.execute("select polls_customer.name as customer_name,          sum(polls_receiptitem.amount * "
                               "polls_receiptitem.price) as spent   from polls_customer   inner join polls_receipt   "
                               "on polls_customer.id = polls_receipt.customer_id   inner join polls_receiptitem   on "
                               "polls_receipt.id = polls_receiptitem.receipt_id   inner join polls_tradepoint   on "
                               "polls_receipt.trade_point_id = polls_tradepoint.id          and "
                               "polls_tradepoint.point_type_id = {0}   group by (polls_customer.id, "
                               "polls_customer.name)   order by spent desc "
                               .format(trade_point_type))
            else:
                cursor.execute("select polls_customer.name as customer_name,          sum(polls_receiptitem.amount * "
                               "polls_receiptitem.price) as spent   from polls_customer   inner join polls_receipt   "
                               "on polls_customer.id = polls_receipt.customer_id   inner join polls_receiptitem   on "
                               "polls_receipt.id = polls_receiptitem.receipt_id   inner join polls_tradepoint   on "
                               "polls_receipt.trade_point_id = polls_tradepoint.id   group by (polls_customer.id, "
                               "polls_customer.name)   order by spent desc")
            data = dict_fetchall(cursor)
    return render(request, 'queries/query14.html', {'form': form, 'data': data, 'warning': warning})


def query15(request):
    if request.method != 'POST':
        return render(request, 'queries/query15.html', {'form': Query15Form(), 'data': None, 'warning': None})
    data = None
    warning = None
    form = Query15Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            trade_point_type = None
            trade_point = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk
            if form.cleaned_data.get("trade_point") is not None:
                trade_point = form.cleaned_data.get("trade_point").pk

            if trade_point_type is None and trade_point is None:
                warning = "You need to specify at least 1 field"
            else:
                if trade_point is not None:
                    if trade_point_type is not None:
                        warning = "Trade point type is ignored because concrete trade point is specified"
                    cursor.execute("select polls_product.name as product_name,          polls_tradepoint.name as "
                                   "trade_point_name,          polls_soldproduct.in_stock as in_stock,          "
                                   "polls_soldproduct.price as price   from polls_soldproduct   inner join "
                                   "polls_tradepoint   on polls_soldproduct.trade_point_id = polls_tradepoint.id      "
                                   "    and polls_tradepoint.id = {0}   inner join polls_product   on "
                                   "polls_soldproduct.product_id = polls_product.id   order by (polls_product.name, "
                                   "polls_tradepoint.name) asc   "
                                   .format(trade_point))
                else:
                    cursor.execute("select polls_product.name as product_name,          polls_tradepoint.name as "
                                   "trade_point_name,          polls_soldproduct.in_stock as in_stock,          "
                                   "polls_soldproduct.price as price   from polls_soldproduct   inner join "
                                   "polls_tradepoint   on polls_soldproduct.trade_point_id = polls_tradepoint.id      "
                                   "    and polls_tradepoint.point_type_id = {0}   inner join polls_product   on "
                                   "polls_soldproduct.product_id = polls_product.id   order by (polls_product.name, "
                                   "polls_tradepoint.name) asc   "
                                   .format(trade_point_type))
                data = dict_fetchall(cursor)
    return render(request, 'queries/query15.html', {'form': form, 'data': data, 'warning': warning})
