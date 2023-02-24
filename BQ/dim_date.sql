select
  date,
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(QUARTER FROM date) AS quarter,
  EXTRACT(MONTH FROM date) AS month,
  EXTRACT(WEEK FROM date) AS week,
  EXTRACT(DAY FROM date) AS day,
  EXTRACT(DAYOFWEEK FROM date) AS day_of_week,
  EXTRACT(DAYOFYEAR FROM date) AS day_of_year,
  FORMAT_DATE('%Y-%m', date) AS year_month,
  FORMAT_DATE('%Y-%m-%d', date) AS date_id,
  CAST(FORMAT_DATE('%Y%m%d', date) AS INT64) AS int_date_id,
  CAST(FORMAT_DATE('%Y%W', date) AS INT64) AS int_week_id,
  CAST(FORMAT_DATE('%Y', date) AS INT64) * 10000 + CAST(FORMAT_DATE('%W', date) AS INT64) AS week_id
from unnest(GENERATE_DATE_ARRAY("2016-06-01", CURRENT_DATE())) as Dates
