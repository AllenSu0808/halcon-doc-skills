# TupleLsh (Operator)

## Name

`TupleLsh` — Shift a tuple bitwise to the left.

## Signature

`static void HOperatorSet.TupleLsh(HTuple t, HTuple shift, out HTuple lsh)`

`HTuple HTuple.TupleLsh(HTuple shift)`

## Description

`TupleLsh` shifts the tuple *`t`* bitwise to the left by
*`shift`* places. If no overflow occurs, this operation is
equivalent to a multiplication by 2^{*`shift`*}. If *`t`*
is negative, the result depends on the hardware. If *`shift`*
is negative or larger than 32, the result is undefined. If both
tuples have the same length the corresponding elements of both
tuples are shifted. Otherwise, either *`t`* or *`shift`*
must have length 1. In this case, the operation is performed for
each element of the longer tuple with the single element of the
other tuple. The input tuples must contain only integer numbers.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleLsh`,
which can be used in an expression in the following syntax:

[`Lsh := lsh(T, Shift)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple.

**`shift`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of places to shift the input tuple.

**`lsh`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Shifted input tuple.

## Alternatives

`TupleMult`

## See also

`TupleRsh`

## Module

Foundation
