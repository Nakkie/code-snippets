with dimdate as
(
select distinct Dates
               ,FORMAT_DATE('%B %E4Y', Dates) as DisplayName
               ,FORMAT_DATE('%E4Y%m', Dates) as OrderMonth
               ,FORMAT_DATE('%E4Y', Dates) as OrderYear
from unnest(GENERATE_DATE_ARRAY("2016-06-01", CURRENT_DATE())) as Dates
),