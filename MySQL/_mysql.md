# MySQL Readme

    - If you are using MySQL 5.7 when reading this, I feel for you bud 

Below are descriptions for the files contained in this directory

## cursor

A cursor template

## events

Creating events because no Job Scheduler, MS SQL really spoils you

## mysql67_rownumber

If you are the person responsible for choosing to run MySQL 5.7, may you burn in hell

This is the answer to not being able to use simple windowing functions, such a row_number()

FAOL

## running_tasks

What's running and how to kill it

If you don't have a mysql.general_log

    1. Sorry that your life sucks
    2. This is why we don't need DBA's

Try turning it [on](https://dev.mysql.com/doc/refman/8.0/en/query-log.html)
