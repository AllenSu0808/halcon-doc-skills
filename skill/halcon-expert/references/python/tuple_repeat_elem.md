# tuple_repeat_elem (Operator)

## Name

`tuple_repeat_elem` — Repeat the elements of a tuple.

## Signature

`def tuple_repeat_elem(tuple: HTupleType, num: Union[int, float]) -> Sequence[HTupleElementType]`

`def tuple_repeat_elem_s(tuple: HTupleType, num: Union[int, float]) -> HTupleElementType`

## Description

`tuple_repeat_elem` repeats each element of *`tuple`*
*`num`* times and returns them with *`result`*. Thus,
*`result`* contains *`num`* times more elements than
*`tuple`*. For example, the first *`num`* elements of
*`result`* are equal to the first element of *`tuple`*.
*`num`* must be positive and integer (also for type `real`). If
*`num`* is equal to 0, an empty tuple is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_repeat_elem`,
which can be used in an expression in the following syntax:

[`Result := rep_elem(Tuple, Num)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` HTupleType

Input tuple.

**`num`** (input_control)  integer `→` Union[int, float]

Number of repetitions.

**`result`** (output_control)  tuple(-array) `→` Sequence[HTupleElementType]

Tuple with repeated elements.

## Example (HDevelop)

```
tuple_repeat_elem (['a', 'b', 'c'], 2, Result)
* Returns ['a', 'a', 'b', 'b', 'c', 'c']
```

## Alternatives

`tuple_concat`,
`tuple_gen_const`

## See also

`tuple_repeat`

## Module

Foundation
