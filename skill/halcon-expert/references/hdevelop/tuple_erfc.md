# tuple_erfc (Operator)

## Name

`tuple_erfc` — Compute the complementary error function of a tuple.

## Signature

`tuple_erfc( : : T : Erfc)`

## Description

`tuple_erfc` computes the complementary error function of the
input tuple *`T`*. The complementary error function is defined
as $1-\text{erf}(x)$ (for the definition of
$\text{erf}(x)$ see [`tuple_erf`](tuple_erf.md)). The value of
the complementary error function is always returned as a floating
point number in *`Erfc`*. The complementary error function of a
string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_erfc`, which
can be used in an expression in the following syntax:

[`Erfc := erfc(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  number(-array) `→`  (real / integer)

Input tuple.

**`Erfc`** (output_control)  number(-array) `→`  (real)

Value of the complementary error function of the input tuple.

## Alternatives

`tuple_erf`

## See also

`tuple_exp`

## Module

Foundation
