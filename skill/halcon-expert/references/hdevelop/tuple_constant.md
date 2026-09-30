# tuple_constant (Operator)

## Name

`tuple_constant` — Generate a tuple with the value of a HDevelop language constant.

## Signature

`tuple_constant( : : Name : Value)`

## Description

`tuple_constant` generates a new tuple with the value of a HDevelop
language constant.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_constant`,
which can be used in an expression in the following syntax:

[`Value := constant(Name)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Attention

H_INT64_MIN and H_INT64_MAX will both produce an error if 32-bit HALCON is
being used, as they cannot be represented in the then 32-bit integer used in
tuples.

H_INT_MIN and H_INT_MAX will produce different values depending on whether
HALCON 32- or 64-bit is being used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Name`** (input_control)  tuple `→`  (string)

The name of the HDevelop language constant as string.

Default:
'H_INT32_MIN'

List of values:
'HNULL', 'H_FLOAT32_EPSILON', 'H_FLOAT32_MAX', 'H_FLOAT32_MIN', 'H_FLOAT32_MIN_POSITIVE', 'H_FLOAT64_EPSILON', 'H_FLOAT64_MAX', 'H_FLOAT64_MIN', 'H_FLOAT64_MIN_POSITIVE', 'H_FLOAT_INFINITY', 'H_FLOAT_NAN', 'H_FLOAT_NEG_INFINITY', 'H_INT32_MAX', 'H_INT32_MIN', 'H_INT64_MAX', 'H_INT64_MIN', 'H_INT_MAX', 'H_INT_MIN', 'H_MSG_FAIL', 'H_MSG_FALSE', 'H_MSG_TRUE', 'H_MSG_VOID', 'H_TYPE_ANY', 'H_TYPE_HANDLE', 'H_TYPE_INT', 'H_TYPE_MIXED', 'H_TYPE_REAL', 'H_TYPE_STRING', 'false', 'true'

**`Value`** (output_control)  tuple `→`  (integer / real / handle)

The value of the constant.

## Module

Foundation
