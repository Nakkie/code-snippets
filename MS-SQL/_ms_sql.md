# MS SQL Readme

Fair warning, I haven't touched MS SQL in a couple of years since I made these... welcome to opensource deving... where the licenses don't exist and the fees are made up.

    - Q: You sure have a lot things that just shows generic data?
    - A: I used that output in some programmatic way at some point in time

    - Q: You seem very biast against DBA's?
    - A: I always knew they could be automated, go checkout Google Cloud SQL

Below are descriptions for the files contained in this directory

## Code_Def

Very simple view of procs n views in a db / server

## Column_Rename

Programmatic rename of columns
Why would you want to do this? Because I had reasons

FAIR WARNING: Very dangerous for many many reasons

## Cursor_Template

A cursor template

## DB_SizeChk

Check the DB size in SSMS, because DBA's are stingy bastards

## Job_History

List jobs that ran on the server

## Last_Restore

Last time a DB was restored, because DBA's restore DBs for some reason or the other without telling people, fuck your changes right?

## Pivot_Templates

Pivot and Unpivot templates, TSQL / variable friendly

## Rollback

Because they never really die

## Scraps

Random stuff I'm too lazy to split out, but will look for at some point

Definition of trash, something you throw away 3 weeks before you need it

## Server_Activity

A bunch of nifty scripts to tell you what is going on

sp_who2, WTF even is this? A sad excuse for [sp_whoisactive](https://www.brentozar.com/archive/2010/09/sql-server-dba-scripts-how-to-find-slow-sql-server-queries/)

    - Jesus, this page is from 2010, how old can a person feel man...

I would also suggest just checking out [Brent Ozar's page](https://www.brentozar.com/) in general, bunch of clever peeps

## Shrink_Log

Shrinks the log, use with care, it will only help that much in the long run

## Table_Constraints

Shows the table constraints

## Table_Meta

Shows meta data about the table, mostly data types

## Table_Space

Shows you how much space the table is taking up

## TSQL_UserLoad

Programmatic load of a user, because the DBA's thought their Kung Fu was better than mine 