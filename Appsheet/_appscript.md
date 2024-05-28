# AppSheet Readme

This folder is going to work a bit differently, I just want to have a list of things and they are small.

## Derefence

When you have a reference column in your table, return the value from the other table in this column

    [YOUR_REF_COLUMN_NAME_IN_THIS_TABLE].[THE_COLUMN_YOU_WANT_FROM_THE_OTHER_TABLE]

## Horrific Sum Example

You can sum fields, this example below shows you how to do it in the most horrific manner possible

    sum(LIST([COL1],[COL2],[COL3],[COL4]))

## Filtering Stuff using a SELECT

    ANY(
    SELECT(
        LOOKUP_TABLE[RETURN_COLUMN],
        AND(
        [LOOKUP_COLUMN_A] <= [_THISROW].[THIS_TABLE_COLUMN_LOOKUP_VALUE],
        [LOOKUP_COLUMN_B] >= [_THISROW].[THIS_TABLE_COLUMN_LOOKUP_VALUE]
        )
    )
    )