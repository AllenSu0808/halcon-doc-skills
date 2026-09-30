# tuple_repeat_elem (Operator)

## Name

`tuple_repeat_elem` — Repeat the elements of a tuple.

## Signature

`tuple_repeat_elem( : : Tuple, Num : Result)`

## Description

`tuple_repeat_elem` repeats each element of *`Tuple`*
*`Num`* times and returns them with *`Result`*. Thus,
*`Result`* contains *`Num`* times more elements than
*`Tuple`*. For example, the first *`Num`* elements of
*`Result`* are equal to the first element of *`Tuple`*.
*`Num`* must be positive and integer (also for type `real`). If
*`Num`* is equal to 0, an empty tuple is returned.

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

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`Num`** (input_control)  integer `→`  (integer / real)

Number of repetitions.

**`Result`** (output_control)  tuple(-array) `→`  (integer / real / string / handle)

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
