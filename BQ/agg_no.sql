--OG JSON OBJECT = [{'id': 10402, 'name': 'Music'}, {'id': 99, 'name': 'Documentary'}]

with stgenres as
(
select imdb_id, split(replace(replace(trim(genres, '[]'),'{',''),'}','')) genres
from datamart_adapt.movies_metadata
limit 10
),

stgenres2 as
(
select imdb_id, replace(replace(grs,"'name': ",''),"'",'') as genres
from stgenres,
unnest (stgenres.genres) as grs
where grs like '%name%'
),

stproduction_companies as
(
select imdb_id, split(replace(replace(trim(production_companies, '[]'),'{',''),'}','')) production_companies
from datamart_adapt.movies_metadata
limit 10
),

stproduction_companies2 as
(
select imdb_id, replace(replace(grs,"'name': ",''),"'",'') as production_companies
from stproduction_companies,
unnest (stproduction_companies.production_companies) as grs
where grs like '%name%'
),

stproduction_countries as
(
select imdb_id, split(replace(replace(trim(production_countries, '[]'),'{',''),'}','')) production_countries
from datamart_adapt.movies_metadata
limit 10
),

stproduction_countries2 as
(
select imdb_id, replace(replace(grs,"'name': ",''),"'",'') as production_countries
from stproduction_countries,
unnest (stproduction_countries.production_countries) as grs
where grs like '%name%'
)


select adult, budget, a.imdb_id, original_language, original_title, popularity, release_date, revenue, runtime, status, tagline, vote_average, vote_count,
ARRAY_AGG( distinct (ifnull(b.genres,'')) ) as genres,
ARRAY_AGG( distinct (ifnull(c.production_countries,'')) ) as production_countries,
ARRAY_AGG( distinct (ifnull(d.production_companies,'')) ) as production_companies
from datamart_adapt.movies_metadata a
left join stgenres2 b on a.imdb_id = b.imdb_id
left join stproduction_countries2 c on a.imdb_id = c.imdb_id
left join stproduction_companies2 d on a.imdb_id = d.imdb_id
group by adult, budget, a.imdb_id, original_language, original_title, popularity, release_date, revenue, runtime, status, tagline, vote_average, vote_count