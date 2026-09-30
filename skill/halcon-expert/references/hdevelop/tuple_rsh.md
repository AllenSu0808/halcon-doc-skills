# tuple_rsh (Operator)

## Name

`tuple_rsh` — Shift a tuple bitwise to the right.

## Signature

`tuple_rsh( : : T, Shift : Rsh)`

## Description

`tuple_rsh` shifts the tuple *`T`* bitwise to the right
by *`Shift`* places. This operation is equivalent to a
division by 2^{*`Shift`*}. If *`T`* is negative, the
result depends on the hardware. If *`Shift`* is negative or
larger than 32, the result is undefined. If both tuples have the
same length the corresponding elements of both tuples are shifted.
Otherwise, either *`T`* or *`Shift`* must have length 1.
In this case, the operation is performed for each element of the
longer tuple with the single element of the other tuple. The input
tuples must contain only integer numbers.

### Exception: Empty input tuple

If any of the input tuples is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_rsh`,
which can be used in an expression in the following syntax:

[`Rsh := rsh(T, Shift)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  integer(-array) `→`  (integer)

Input tuple.

**`Shift`** (input_control)  integer(-array) `→`  (integer)

Number of places to shift the input tuple.

**`Rsh`** (output_control)  integer(-array) `→`  (integer)

Shifted input tuple.

## Alternatives

`tuple_div`

## See also

`tuple_lsh`

## Module

Foundation
