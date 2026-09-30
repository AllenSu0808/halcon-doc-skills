# tuple_add (Operator)

## Name

`tuple_add` — Add two tuples.

## Signature

`def tuple_add(s1: MaybeSequence[Union[float, int, str]], s2: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

`def tuple_add_s(s1: MaybeSequence[Union[float, int, str]], s2: MaybeSequence[Union[float, int, str]]) -> Union[float, int, str]`

## Description

`tuple_add` computes the sum of the input tuples *`s1`*
and *`s2`*. If both tuples have the same length the
corresponding elements of both tuples are added. Otherwise, either
*`s1`* or *`s2`* must have length 1. In this case, the
addition is performed for each element of the longer tuple with the
single element of the other tuple. If two integer numbers are
added, the result is again an integer number. If a floating point
number is added to another number, the result is a floating point
number. If two strings are added, the addition corresponds to a
string concatenation. If a number and a string are added, the
number is converted to a string first. Thus, the addition also
corresponds to a string concatenation in this case.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_add`,
which can be used in an expression in the following syntax:

[`Sum := S1 + S2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_arithmetic_0000.html)

The `+` operation corresponds to a
[string concatenation](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)
if *`s1`* and *`s2`* contain strings.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`s1`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple 1.

**`s2`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple 2.

**`sum`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Sum of the input tuples.

## Alternatives

`tuple_sub`

## See also

`tuple_cumul`

## Module

Foundation
