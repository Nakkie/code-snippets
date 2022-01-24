# Specific Tasks

## Merge Join Transformation

The Merge Join Transformation in SSIS is used to perform SQL Joins such as;

    Inner Join, 
    Left Outer Join, 
    Full Outer Join, 
    and Right Outer Join in SQL Server Integration Services.

The Merge Join Transformation in SSIS will only work with Sorted data.

This transformation has two inputs and one output. 
It does not support an error output.

On configuration specify Join type and Join Key.

## Sort Transformation

The Sort transformation sorts input data in ascending or descending order and copies the sorted data to the transformation output. 
You can apply multiple sorts to an input; each sort is identified by a numeral that determines the sort order.

Columns that are not selected for sorting are automatically copied to the transformation output together with the sorted columns.

Passthrough selects column for sorting.
On configuration specify Sort type and Sort Order.
Can change input column to output alias.

The Sort transformation can also remove duplicate rows as part of its sort.

## Multicast Transformation

The Multicast transformation distributes its input to one or more outputs. This transformation is similar to the Conditional Split transformation. Both transformations direct an input to multiple outputs. The difference between the two is that the Multicast transformation directs every row to every output, and the Conditional Split directs a row to a single output.

Using the Multicast transformation, a package can create logical copies of data. This capability is useful when the package needs to apply multiple sets of transformations to the same data. For example, one copy of the data is aggregated and only the summary information is loaded into its destination, while another copy of the data is extended with lookup values and derived columns before it is loaded into its destination.

tl;dr Multiple destinations, same data.

## Conditional Split Transformation

The Conditional Split transformation can route data rows to different outputs depending on the content of the data. The implementation of the Conditional Split transformation is similar to a CASE decision structure in a programming language. The transformation evaluates expressions, and based on the results, directs the data row to the specified output. This transformation also provides a default output, so that if a row matches no expression it is directed to the default output.

You can configure the Conditional Split transformation in the following ways:

    Provide an expression that evaluates to a Boolean for each condition you want the transformation to test.

    Specify the order in which the conditions are evaluated. 
    Order is significant, because a row is sent to the output corresponding to the first condition that evaluates to true.

    Specify the default output for the transformation. 
    The transformation requires that a default output be specified.

    Output 1

    SUBSTRING(FirstName,1,1) == "A"

    Output 2

    SUBSTRING(FirstName,1,1) == "B"

tl;dr Multiple destinations, subsets of OG data.

## Derived Column Transformation

The Derived Column transformation creates new column values by applying expressions to transformation input columns. 

An expression can contain any combination of; 
    variables, 
    functions, 
    operators, 
    and columns from the transformation input.

The result can be added as a new column or inserted into an existing column as a replacement value.

The Derived Column transformation can define;
    multiple derived columns,
     and any variable or, 
     input columns can appear in multiple expressions.

You can use this transformation to perform the following tasks;
    Concatenate
    SUBSTRING
    mathematical functions
    compare input columns and variables
    DATEPART

## Aggregate Transformation

You configure the Aggregate transformation at the transformation, output, and column levels.

    At the transformation level, you configure the Aggregate transformation for performance by specifying the following values:

        The number of groups that are expected to result from a Group by operation.

        The number of distinct values that are expected to result from a Count distinct operation.

        The percentage by which memory can be extended during the aggregation.

    The Aggregate transformation can also be configured to generate a warning instead of failing when the value of a divisor is zero.

    At the output level, you configure the Aggregate transformation for performance by specifying the number of groups that are expected to result from a Group by operation. The Aggregate transformation supports multiple outputs, and each can be configured differently.

    At the column level, you specify the following values:

        The aggregation that the column performs.

        The comparison options of the aggregation.

You can also configure the Aggregate transformation for performance by specifying these values:

    The number of groups that are expected to result from a Group by operation on the column.

    The number of distinct values that are expected to result from a Count distinct operation on the column.

You can also identify columns as IsBig if a column contains large numeric values or numeric values with high precision.

The Aggregate transformation is asynchronous, which means that it does not consume and publish data row by row. Instead it consumes the whole rowset, performs its groupings and aggregations, and then publishes the results.

## Character Map Transformation

The Character Map transformation applies string functions, such as conversion from lowercase to uppercase, to character data. This transformation operates only on column data with a string data type.

The Character Map transformation can convert column data in place or add a column to the transformation output and put the converted data in the new column. You can apply different sets of mapping operations to the same input column and put the results in different columns. For example, you can convert the same column to uppercase and lowercase and put the results in two different columns.

Mapping can, under some circumstances, cause data to be truncated.

## Import Column Transformation

The Import Column transformation reads data from files and adds the data to columns in a data flow. Using this transformation, a package can add text and images stored in separate files to a data flow.

## Export Column Transformation

The Export Column transformation reads data in a data flow and inserts the data into a file. For example, if the data flow contains product information, such as a picture of each product, you could use the Export Column transformation to save the images to files.

## Fuzzy Grouping Transformation

The Fuzzy Grouping transformation performs data cleaning tasks by identifying rows of data that are likely to be duplicates and selecting a canonical row of data to use in standardizing the data.

The Fuzzy Grouping transformation requires a connection to an instance of SQL Server to create the temporary SQL Server tables that the transformation algorithm requires to do its work. The connection must resolve to a user who has permission to create tables in the database.

The transformation produces one output row for each input row, with the following additional columns:

    _key_in, a column that uniquely identifies each row.

    _key_out, a column that identifies a group of duplicate rows. The _key_out column has the value of the _key_in column in the canonical data row. Rows with the same value in _key_out are part of the same group. The _key_outvalue for a group corresponds to the value of _key_in in the canonical data row.

    _score, a value between 0 and 1 that indicates the similarity of the input row to the canonical row.

When you configure the Fuzzy Grouping transformation, you can specify the comparison algorithm that the transformation uses to compare rows in the transformation input.

## Fuzzy Lookup Transformation

The Fuzzy Lookup transformation performs data cleaning tasks such as standardizing data, correcting data, and providing missing values.

The transformation output columns include the input columns that are marked as pass-through columns, the selected columns in the lookup table, and the following additional columns:

    _Similarity, a column that describes the similarity between values in the input and reference columns.

    _Confidence, a column that describes the quality of the match.

The transformation uses the connection to the SQL Server database to create the temporary tables that the fuzzy matching algorithm uses.

## Lookup Transformation

The Lookup transformation performs lookups by joining data in input columns with columns in a reference dataset.

You can configure the Lookup transformation in the following ways:

    Select the connection manager that you want to use. If you want to connect to a database, select an OLE DB connection manager. If you want to connect to a cache file, select a Cache connection manager.

    Specify the table or view that contains the reference dataset.

    Generate a reference dataset by specifying an SQL statement.

    Specify joins between the input and the reference dataset.

    Add columns from the reference dataset to the Lookup transformation output.

    Configure the caching options.

The Lookup transformation supports the following database providers for the OLE DB connection manager:

    SQL Server

    Oracle

    DB2

The Lookup transformation tries to perform an equi-join between values in the transformation input and values in the reference dataset. (An equi-join means that each row in the transformation input must match at least one row from the reference dataset.) If an equi-join is not possible, the Lookup transformation takes one of the following actions:

    If there is no matching entry in the reference dataset, no join occurs. By default, the Lookup transformation treats rows without matching entries as errors. However, you can configure the Lookup transformation to redirect such rows to a no match output.

    If there are multiple matches in the reference table, the Lookup transformation returns only the first match returned by the lookup query. If multiple matches are found, the Lookup transformation generates an error or warning only when the transformation has been configured to load all the reference dataset into the cache. In this case, the Lookup transformation generates a warning when the transformation detects multiple matches as the transformation fills the cache.

The join can be a composite join.

## Merge Transformation

The Merge transformation combines two sorted datasets into a single dataset. The rows from each dataset are inserted into the output based on values in their key columns.

By including the Merge transformation in a data flow, you can perform the following tasks:

    Merge data from two data sources, such as tables and files.

    Create complex datasets by nesting Merge transformations.

    Remerge rows after correcting errors in the data.

The Merge transformation is similar to the Union All transformations. Use the Union All transformation instead of the Merge transformation in the following situations:

    The transformation inputs are not sorted.

    The combined output does not need to be sorted.

    The transformation has more than two inputs.

The Merge Transformation requires sorted data for its inputs.

The Merge transformation also requires that the merged columns in its inputs have matching metadata.
