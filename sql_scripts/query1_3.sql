select *
from (select polls_distributor.name as distributor_name,
             sum(distr_product.amount) as product_amount
      from polls_distributor
      inner join (select *
                  from polls_productorderitem
                  inner join polls_productsorder
                  on polls_productorderitem.products_order_id = polls_productsorder.id
                      and polls_productsorder.date >= '2010-01-01'
                      and polls_productsorder.date <= '2022-12-12'
                  inner join polls_distributorproduct
                  on polls_productorderitem.distributor_product_id = polls_distributorproduct.id
                  where polls_distributorproduct.product_id = 88) as distr_product
      on polls_distributor.id = distr_product.distributor_id
      group by (polls_distributor.id, polls_distributor.name)) as distr_product_amount
where distr_product_amount.product_amount >= 10