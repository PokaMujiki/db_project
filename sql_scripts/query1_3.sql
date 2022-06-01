select distr_product.distributor_name as distributor_name, sum(polls_productorderitem.amount) as product_amount, polls_productorderitem.price as product_price
from polls_productorderitem inner join (
    select polls_productsorder.id as order_id, polls_productsorder.date as order_date
    from polls_productsorder
    where polls_productsorder.date >= '2021-08-01' and polls_productsorder.date <= '2021-09-01') as orders
on polls_productorderitem.products_order_id = orders.order_id
inner join (
    select polls_product.id as product_id, polls_distributor.name as distributor_name, polls_distributorproduct.id as distributorproduct_id, polls_distributor.id as distributor_id
    from polls_distributorproduct inner join polls_product
    on polls_distributorproduct.product_id = polls_product.id
    inner join polls_distributor on polls_distributor.id = polls_distributorproduct.distributor_id) as distr_product
on distr_product.product_id = 88 and distr_product.distributorproduct_id = polls_productorderitem.distributor_product_id
where polls_productorderitem.amount >= 1
group by (distributor_id, distributor_name, product_price)
