import datetime

from django.db import connection
from django.shortcuts import render

from .forms import *


def dict_fetchall(cursor):
    print("Asdasda")
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def query1(request):
    data = None
    error = None
    complicated_view = None

    if request.method == 'POST':
        form = Query1Form(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                required_product = form.cleaned_data.get("required_product").pk
                volume = form.cleaned_data.get("volume")
                start_date = form.cleaned_data.get("start_date")
                end_date = form.cleaned_data.get("end_date")

                print("volume " + str(volume))
                print("start date " + str(start_date))
                print("end date " + str(end_date))

                if (start_date is None and end_date is not None) or (start_date is not None and end_date is None):
                    error = "Error in date input fields"
                else:
                    if volume is None:
                        cursor.execute("select polls_distributor.name as distributor_name from polls_distributor "
                                       "inner join polls_distributorproduct on "
                                       "polls_distributorproduct.distributor_id = polls_distributor.id where "
                                       "polls_distributorproduct.product_id = {0} group by "
                                       "polls_distributor.id".format(required_product))
                    elif start_date is None and end_date is None:
                        complicated_view = True
                        cursor.execute("select distr_product.distributor_name as distributor_name, "
                                       "sum(polls_productorderitem.amount) as product_amount, "
                                       "polls_productorderitem.price as product_price  from polls_productorderitem "
                                       "inner join (      select polls_productsorder.id as order_id, "
                                       "polls_productsorder.date as order_date      from polls_productsorder) as "
                                       "orders  on polls_productorderitem.products_order_id = orders.order_id  inner "
                                       "join (      select polls_product.id as product_id, polls_distributor.name as "
                                       "distributor_name, polls_distributorproduct.id as distributorproduct_id, "
                                       "polls_distributor.id as distributor_id      from polls_distributorproduct "
                                       "inner join polls_product      on polls_distributorproduct.product_id = "
                                       "polls_product.id      inner join polls_distributor on polls_distributor.id = "
                                       "polls_distributorproduct.distributor_id) as distr_product  on "
                                       "distr_product.product_id = {0} and distr_product.distributorproduct_id = "
                                       "polls_productorderitem.distributor_product_id  where "
                                       "polls_productorderitem.amount >= {1}  group by (distributor_id, "
                                       "distributor_name, product_price) "
                                       .format(required_product, volume))
                    else:
                        complicated_view = True
                        cursor.execute("select distr_product.distributor_name as distributor_name, "
                                       "sum(polls_productorderitem.amount) as product_amount, "
                                       "polls_productorderitem.price as product_price  from polls_productorderitem "
                                       "inner join (      select polls_productsorder.id as order_id, "
                                       "polls_productsorder.date as order_date      from polls_productsorder      "
                                       "where polls_productsorder.date >= '{2}' and polls_productsorder.date "
                                       "<= '{3}') as orders  on polls_productorderitem.products_order_id = "
                                       "orders.order_id  inner join (      select polls_product.id as product_id, "
                                       "polls_distributor.name as distributor_name, polls_distributorproduct.id as "
                                       "distributorproduct_id, polls_distributor.id as distributor_id      from "
                                       "polls_distributorproduct inner join polls_product      on "
                                       "polls_distributorproduct.product_id = polls_product.id      inner join "
                                       "polls_distributor on polls_distributor.id = "
                                       "polls_distributorproduct.distributor_id) as distr_product  on "
                                       "distr_product.product_id ={0} and distr_product.distributorproduct_id = "
                                       "polls_productorderitem.distributor_product_id  where "
                                       "polls_productorderitem.amount >= {1}  group by (distributor_id, "
                                       "distributor_name, product_price) "
                                       .format(required_product, volume, start_date, end_date))
                    data = dict_fetchall(cursor)
    else:
        form = Query1Form()
    return render(request, 'queries/query1.html', {'form': form, 'data': data, 'error': error,
                                                   'complicated_view': complicated_view})


def query2(request):
    data = None
    warning = None
    complicated_view = None

    if request.method == 'POST':
        form = Query2Form(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                required_product = form.cleaned_data.get("required_product").pk
                volume = form.cleaned_data.get("volume")
                start_date = form.cleaned_data.get("start_date")
                end_date = form.cleaned_data.get("end_date")

                print("volume " + str(volume))
                print("start date " + str(start_date))
                print("end date " + str(end_date))

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
                                       "polls_customer.id = polls_receipt.customer_id  where items.amount > {1}  group "
                                       "by (polls_customer.id, polls_customer.name) "
                                       .format(required_product, volume))
                    elif start_date is not None and end_date is not None:
                        # if datetime.strptime(start_date, "%Y-%m-%d") >= datetime.datetime(end_date):
                        #     warning = "Bad date input fields"
                        # TODO start time < date time check 
                        # else:
                        cursor.execute("select polls_customer.name as customer_name from polls_receipt inner join "
                                       "(     select *     from polls_receiptitem     where "
                                       "polls_receiptitem.product_id = 4) as items on polls_receipt.id = "
                                       "items.receipt_id and polls_receipt.date >= '2010-01-01' and "
                                       "polls_receipt.date <= '2022-12-12' inner join polls_customer on "
                                       "polls_customer.id = polls_receipt.customer_id group by ("
                                       "polls_customer.id, polls_customer.name) "
                                       .format(required_product, start_date, end_date))
                    else:
                        warning = "Please, specify date correctly"
                    data = dict_fetchall(cursor)
    else:
        form = Query2Form()
    return render(request, 'queries/query2.html', {'form': form, 'data': data, 'warning': warning,
                                                   'complicated_view': complicated_view})


def query3(request):
    data = None

    if request.method != 'POST':
        form = Query3Form()
    else:
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
    return render(request, 'queries/query3.html', {'form': form, 'data': data})


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
        return render(request, 'queries/query5.html', {'form': Query5Form(), 'data': None})
    data = None
    form = Query5Form(request.POST)
    if form.is_valid():
        with connection.cursor() as cursor:
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            trade_point_type = None
            if form.cleaned_data.get("trade_point_type") is not None:
                trade_point_type = form.cleaned_data.get("trade_point_type").pk
            # todo START DATE > END DATE CHECK
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
    return render(request, 'queries/query5.html', {'form': form, 'data': data})
