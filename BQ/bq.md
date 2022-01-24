# BQ Readme

This folder contains the following SQL files;

    - dim_date
    - ml_matrix_factorization
    - pivot

## dim_date

Simple in-query date dimension generator

## ml_matrix_factorization

Toying around with doing ML in BQ

Note: Matrix factorization models are only available to flat-rate customers or customers with reservations. On-demand customers are encouraged to use flex slots to use matrix factorization.

[BQ MF Docs Page](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-matrix-factorization)

## pivot

Because BQ no pivot (back in the day)

[This has changed in recent years](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#pivot_operator)