# TupleIsMixed (Operator)

## Name

`TupleIsMixed` — Test whether a tuple is of type `mixed`.

## Signature

`static void HOperatorSet.TupleIsMixed(HTuple t, out HTuple isMixed)`

`HTuple HTuple.TupleIsMixed()`

## Description

`TupleIsMixed` tests the input tuple *`t`*.
If the type is `mixed`, the value *1* (true) is returned in
*`isMixed`*, else *0* (false) is returned. If a tuple consists of
elements with equal data types only, *`isMixed`* can nevertheless be 1
in case the internal representation is H_TYPE_MIXED; see
[`TupleType`](tuple_type.md) for details.

If the type of the tuple is `mixed` and you need all elements of
the tuple *`t`* to be of one data type only, you can
explicitly convert the tuple to a better fitting
representation by using [`TupleInt`](tuple_int.md), [`TupleReal`](tuple_real.md) or
[`TupleString`](tuple_string.md) with Format='s'. This improves processing speed for the
converted tuple which is especially useful if the tuple is used many times
afterwards.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 1.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsMixed`,
which can be used in an expression in the following syntax:

[`IsMixed := is_mixed(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Input tuple.

**`isMixed`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Is the input tuple of type `mixed`?

## Example (HDevelop)

```
tuple_is_mixed ([3.1416,'pi',3], IsMixedA)
* IsMixedA = true
tuple_is_mixed (['a','b','111'], IsMixedB)
* IsMixedB = false
tuple_is_mixed ([], IsMixedC)
* IsMixedC = true
```

## Result

If the parameters are valid, the operator
`TupleIsMixed` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleIsNumber`

## See also

`TupleIsInt`,
`TupleIsReal`

## Module

Foundation
