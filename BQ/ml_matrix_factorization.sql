-- create source view for BQ Filtering ML
CREATE OR REPLACE VIEW recommender.vw_product_ratings as
select b.customer_id,
       a.product_id,
       count(distinct order_numbers) as product_rating
from test_data_clean.dim_product a
left join test_data_clean.fct_sales b on safe_cast(a.product_id as string) = b.product_id
group by b.customer_id,
         a.product_id;

-- create filtering ML model in BQ
CREATE OR REPLACE MODEL recommender.catalog_filter
        OPTIONS (
            model_type='matrix_factorization',
            user_col='customer_id',
            item_col='product_id',
            rating_col='product_rating',
            num_factors=5
        ) AS
            select *
            from recommender.vw_product_ratings;
