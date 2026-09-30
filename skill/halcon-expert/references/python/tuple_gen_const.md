# tuple_gen_const (Operator)

## Name

`tuple_gen_const` — Generate a tuple of a specific length and initialize its elements.

## Signature

`def tuple_gen_const(length: Union[float, int], const: HTupleElementType) -> Sequence[Union[float, int, str]]`

`def tuple_gen_const_s(length: Union[float, int], const: HTupleElementType) -> Union[float, int, str]`

## Description

`tuple_gen_const` generates a new tuple in *`newtuple`*.
The input parameter *`length`* determines the number of elements
for the new tuple. Thus, *`length`* may only consist of a single number.
If *`length`* contains a floating point number, this may only
represent an integer value (without fraction).
The data type and value of each element of the new generated tuple is
determined by the input parameter *`const`* that may only
consist of a single element. All elements in *`newtuple`*
have got the same data type and value as the single element in
*`const`*.

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

**`length`** (input_control)  number `→` Union[float, int]

Length of tuple to generate.

**`const`** (input_control)  tuple `→` HTupleElementType

Constant for initializing the tuple elements.

**`newtuple`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

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
