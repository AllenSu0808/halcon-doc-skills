# tuple_is_mixed (Operator)

## Name

`tuple_is_mixed` — Test whether a tuple is of type `mixed`.

## Signature

`tuple_is_mixed( : : T : IsMixed)`

## Description

`tuple_is_mixed` tests the input tuple *`T`*.
If the type is `mixed`, the value *1* (true) is returned in
*`IsMixed`*, else *0* (false) is returned. If a tuple consists of
elements with equal data types only, *`IsMixed`* can nevertheless be 1
in case the internal representation is H_TYPE_MIXED; see
[`tuple_type`](tuple_type.md) for details.

If the type of the tuple is `mixed` and you need all elements of
the tuple *`T`* to be of one data type only, you can
explicitly convert the tuple to a better fitting
representation by using [`tuple_int`](tuple_int.md), [`tuple_real`](tuple_real.md) or
[`tuple_string`](tuple_string.md) with Format='s'. This improves processing speed for the
converted tuple which is especially useful if the tuple is used many times
afterwards.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 1.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_mixed`,
which can be used in an expression in the following syntax:

[`IsMixed := is_mixed(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (string / real / integer / handle)

Input tuple.

**`IsMixed`** (output_control)  number `→`  (integer)

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
`tuple_is_mixed` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_is_number`

## See also

`tuple_is_int`,
`tuple_is_real`

## Module

Foundation
