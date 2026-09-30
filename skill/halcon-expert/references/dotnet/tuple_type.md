# TupleType (Operator)

## Name

`TupleType` — Return the type of a tuple.

## Signature

`static void HOperatorSet.TupleType(HTuple t, out HTuple type)`

`HTuple HTuple.TupleType()`

## Description

`TupleType` returns the type of the input tuple *`t`*. The type
is returned as an integer value in the output parameter *`type`*. In
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
- the tuple *`t`* has undergone operations which modified the
  data type of single elements. Such tuples will generally not be
  optimized automatically (because of runtime reasons) even if the
  data types of all elements
  become equal in subsequent operations. See [`TupleIsMixed`](tuple_is_mixed.md)
  and the following example on how to optimize such tuples.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 31 (H_TYPE_ANY).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleType`,
which can be used in an expression in the following syntax:

[`Type := type(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

`TupleType` returns the internal data type of the tuple. In contrast
to [`TupleIsNumber`](tuple_is_number.md) it does not return whether a tuple could be
represented as a tuple of a certain type.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string / HHandle)

Input tuple.

**`type`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

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
`TupleType` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleIsInt`,
`TupleIsNumber`,
`TupleIsReal`,
`TupleIsString`,
`TupleSemType`

## See also

`GetObjClass`

## Module

Foundation
