# tuple_gen_const (Operator)

## Name

`tuple_gen_const` — Generate a tuple of a specific length and initialize its elements.

## Signature

`tuple_gen_const( : : Length, Const : Newtuple)`

## Description

`tuple_gen_const` generates a new tuple in *`Newtuple`*.
The input parameter *`Length`* determines the number of elements
for the new tuple. Thus, *`Length`* may only consist of a single number.
If *`Length`* contains a floating point number, this may only
represent an integer value (without fraction).
The data type and value of each element of the new generated tuple is
determined by the input parameter *`Const`* that may only
consist of a single element. All elements in *`Newtuple`*
have got the same data type and value as the single element in
*`Const`*.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_gen_const`,
which can be used in an expression in the following syntax:

[`Newtuple := gen_tuple_const(Length, Const)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Length`** (input_control)  number `→`  (integer / real)

Length of tuple to generate.

**`Const`** (input_control)  tuple `→`  (integer / real / string / handle)

Constant for initializing the tuple elements.

**`Newtuple`** (output_control)  tuple(-array) `→`  (integer / real / string)

New Tuple.

## Alternatives

`tuple_str_bit_select`,
`tuple_select`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_concat`,
`tuple_insert`,
`tuple_replace`,
`tuple_gen_sequence`

## See also

`tuple_rand`

## Module

Foundation
