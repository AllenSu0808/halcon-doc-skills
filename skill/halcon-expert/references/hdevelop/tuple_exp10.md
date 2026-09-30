# tuple_exp10 (Operator)

## Name

`tuple_exp10` — Compute the base 10 exponential of a tuple.

## Signature

`tuple_exp10( : : T : Exp)`

## Description

`tuple_exp10` computes the base 10 exponential of the input
tuple *`T`*. The exponential is always returned as a floating
point number. The exponential of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_exp10`,
which can be used in an expression in the following syntax:

[`Exp := exp10(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Exp`** (output_control)  number(-array) `→`  (real)

Base 10 exponential of the input tuple.

## Alternatives

`tuple_exp`,
`tuple_exp2`,
`tuple_pow`

## See also

`tuple_log`,
`tuple_log2`,
`tuple_log10`

## Module

Foundation
