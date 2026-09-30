# tuple_type (Operator)

## Name

`tuple_type` — Return the type of a tuple.

## Signature

`tuple_type( : : T : Type)`

## Description

`tuple_type` returns the type of the input tuple *`T`*. The type
is returned as an integer value in the output parameter *`Type`*. In
HDevelop corresponding constants are defined:

- H_TYPE_INT (1).
- H_TYPE_REAL (2).
- H_TYPE_STRING (4).
- H_TYPE_MIXED (8).
- H_TYPE_HANDLE (16).
- H_TYPE_ANY (31).

H_TYPE_MIXED is returned in the following two cases:

- some elements of the tuple have different data types, e.g.,
  `real` and `integer`.
- the tuple *`T`* has undergone operations which modified the
  data type of single elements. Such tuples will generally not be
  optimized automatically (because of runtime reasons) even if the
  data types of all elements
  become equal in subsequent operations. See [`tuple_is_mixed`](tuple_is_mixed.md)
  and the following example on how to optimize such tuples.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 31 (H_TYPE_ANY).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_type`,
which can be used in an expression in the following syntax:

[`Type := type(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

`tuple_type` returns the internal data type of the tuple. In contrast
to [`tuple_is_number`](tuple_is_number.md) it does not return whether a tuple could be
represented as a tuple of a certain type.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (real / integer / string / handle)

Input tuple.

**`Type`** (output_control)  number `→`  (integer)

Type of the input tuple as an integer number.

## Example (HDevelop)

```
tuple_type ([3.1416,'pi',3], TypeA)
* TypeA = H_TYPE_MIXED
tuple_type (['a','b','111'], TypeB)
* TypeB = H_TYPE_STRING
tuple_type ([], TypeC)
* TypeC = H_TYPE_ANY
tuple_type (HNULL, TypeD)
* TypeD = H_TYPE_HANDLE

TupleInt := [1,2,3,4]
TupleReal := [42.0]
TupleConcat := [TupleInt, TupleReal]
tuple_type (TupleConcat, TypeConcat)
* TypeConcat = H_TYPE_MIXED
* Now set 42.0 to 42
TupleConcat[4] := 42
tuple_type (TupleConcat, TypeConcat2)
* TypeConcat2 = H_TYPE_MIXED
* TupleConcat now consists of integers only, but the
* internal representation hasn't been updated. Optimize
* it by converting the tuple explicitly to an integer
* tuple.
tuple_int (TupleConcat, TupleConcatInt)
tuple_type (TupleConcatInt, TypeConcatInt)
* TypeConcatInt = H_TYPE_INT
```

## Result

If the parameters are valid, the operator
`tuple_type` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_is_int`,
`tuple_is_number`,
`tuple_is_real`,
`tuple_is_string`,
`tuple_sem_type`

## See also

`get_obj_class`

## Module

Foundation
