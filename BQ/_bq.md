# BQ Readme

Below are descriptions for the files contained in this directory

## agg_no

An horrific attempt at playing with some IMDB data

## bq_query_sizes

Provides a view of queries run on a project with the data size for each

Needed to troubleshoot the most expensive queries for a client

Doesn't have to run in python, just grab the select statement in line 19

## bq_table_sizes

Provides a view of table sizes in BQ

Needed to troubleshoot the most expensive queries for a client

Doesn't have to run in python, just grab the select statement in line 19

## dim_date

Simple in-query date dimension generator

Have reiterated over this a few times, I just keep adding the latest version I use

## ml_matrix_factorization

Toying around with doing ML in BQ

Note: Matrix factorization models are only available to flat-rate customers or customers with reservations. On-demand customers are encouraged to use flex slots to use matrix factorization.

[BQ MF Docs Page](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-matrix-factorization)

## pivot

Because BQ no pivot (back in the day)

[This has changed in recent years](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#pivot_operator)

## upload_csv_to_gbq

Exactly what is says on the box, uploads CSV to BQ using Python and Pandas

I like using Pandas for this, allows for cleaning up field names
And native upload to BQ

