select
  Dates,
  EXTRACT(YEAR FROM Dates) AS year,
  EXTRACT(QUARTER FROM Dates) AS quarter,
  EXTRACT(MONTH FROM Dates) AS month,
  EXTRACT(WEEK FROM Dates) AS week,
  EXTRACT(DAY FROM Dates) AS day,
  EXTRACT(DAYOFWEEK FROM Dates) AS day_of_week,
  EXTRACT(DAYOFYEAR FROM Dates) AS day_of_year,
  FORMAT_DATE('%Y-%m', Dates) AS year_month,
  FORMAT_DATE('%Y-%m-%d', Dates) AS date_id,
  CAST(FORMAT_DATE('%Y%m%d', Dates) AS INT64) AS int_date_id,
  CAST(FORMAT_DATE('%Y%W', Dates) AS INT64) AS int_week_id,
  CAST(FORMAT_DATE('%Y', Dates) AS INT64) * 10000 + CAST(FORMAT_DATE('%W', Dates) AS INT64) AS week_id
from unnest(GENERATE_DATE_ARRAY("2016-06-01", CURRENT_DATE())) as Dates
