# TupleLength (Operator)

## Name

`TupleLength` — Return the number of elements of a tuple.

## Signature

`static void HOperatorSet.TupleLength(HTuple tuple, out HTuple length)`

`HTuple HTuple.TupleLength()`

## Description

`TupleLength` returns the number of elements of the input tuple
*`tuple`*.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 0.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleLength`,
which can be used in an expression in the following syntax:

[`Length := |Tuple|`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`length`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of elements of input tuple.

## Alternatives

`TupleMin`,
`TupleMax`,
`TupleMean`,
`TupleDeviation`,
`TupleSum`,
`TupleMedian`

## See also

`TupleType`

## Module

Foundation
