# tuple_log (Operator)

## Name

`tuple_log` — Compute the natural logarithm of a tuple.

## Signature

`tuple_log( : : T : Log)`

## Description

`tuple_log` computes the natural logarithm of the input tuple
*`T`*. The natural logarithm is always returned as a floating
point number. The natural logarithm of a string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_log`,
which can be used in an expression in the following syntax:

[`Log := log(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

Restriction:
`T > 0`

**`Log`** (output_control)  number(-array) `→`  (real)

Natural logarithm of the input tuple.

## Alternatives

`tuple_log2`,
`tuple_log10`

## See also

`tuple_exp`,
`tuple_exp2`,
`tuple_exp10`,
`tuple_pow`

## Module

Foundation
