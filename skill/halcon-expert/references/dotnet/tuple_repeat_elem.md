# TupleRepeatElem (Operator)

## Name

`TupleRepeatElem` — Repeat the elements of a tuple.

## Signature

`static void HOperatorSet.TupleRepeatElem(HTuple tuple, HTuple num, out HTuple result)`

`HTuple HTuple.TupleRepeatElem(HTuple num)`

## Description

`TupleRepeatElem` repeats each element of *`tuple`*
*`num`* times and returns them with *`result`*. Thus,
*`result`* contains *`num`* times more elements than
*`tuple`*. For example, the first *`num`* elements of
*`result`* are equal to the first element of *`tuple`*.
*`num`* must be positive and integer (also for type `real`). If
*`num`* is equal to 0, an empty tuple is returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleRepeatElem`,
which can be used in an expression in the following syntax:

[`Result := rep_elem(Tuple, Num)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`num`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / double)

Number of repetitions.

**`result`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Tuple with repeated elements.

## Example (HDevelop)

```
tuple_repeat_elem (['a', 'b', 'c'], 2, Result)
* Returns ['a', 'a', 'b', 'b', 'c', 'c']
```

## Alternatives

`TupleConcat`,
`TupleGenConst`

## See also

`TupleRepeat`

## Module

Foundation
