# tuple_lsh (Operator)

## Name

`tuple_lsh` — Shift a tuple bitwise to the left.

## Signature

`def tuple_lsh(t: MaybeSequence[int], shift: MaybeSequence[int]) -> Sequence[int]`

`def tuple_lsh_s(t: MaybeSequence[int], shift: MaybeSequence[int]) -> int`

## Description

`tuple_lsh` shifts the tuple *`t`* bitwise to the left by
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

HDevelop provides an in-line operation for `tuple_lsh`,
which can be used in an expression in the following syntax:

[`Lsh := lsh(T, Shift)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_bit_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  integer(-array) `→` MaybeSequence[int]

Input tuple.

**`shift`** (input_control)  integer(-array) `→` MaybeSequence[int]

Number of places to shift the input tuple.

**`lsh`** (output_control)  integer(-array) `→` Sequence[int]

Shifted input tuple.

## Alternatives

`tuple_mult`

## See also

`tuple_rsh`

## Module

Foundation
