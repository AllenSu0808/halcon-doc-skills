# TupleErfc (Operator)

## Name

`TupleErfc` — Compute the complementary error function of a tuple.

## Signature

`static void HOperatorSet.TupleErfc(HTuple t, out HTuple erfc)`

`HTuple HTuple.TupleErfc()`

## Description

`TupleErfc` computes the complementary error function of the
input tuple *`t`*. The complementary error function is defined
as $1-\text{erf}(x)$ (for the definition of
$\text{erf}(x)$ see [`TupleErf`](tuple_erf.md)). The value of
the complementary error function is always returned as a floating
point number in *`erfc`*. The complementary error function of a
string is not allowed.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleErfc`, which
can be used in an expression in the following syntax:

[`Erfc := erfc(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_exponential_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input tuple.

**`erfc`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Value of the complementary error function of the input tuple.

## Alternatives

`TupleErf`

## See also

`TupleExp`

## Module

Foundation
