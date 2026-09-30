# tuple_repeat (Operator)

## Name

`tuple_repeat` — Repeat a tuple.

## Signature

`tuple_repeat( : : Tuple, Num : Result)`

## Description

`tuple_repeat` repeats *`Tuple`* *`Num`* times and
returns them with *`Result`*. Thus, *`Result`* contains
*`Num`* times more elements than *`Tuple`*. For example, the first
*`Num`* elements of *`Result`* are element-wise equal to the
elements of *`Tuple`*. *`Num`* must be positive and integer (also
for type `real`). If *`Num`* is equal to 0, an empty tuple is
returned.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_repeat`,
which can be used in an expression in the following syntax:

[`Result := rep(Tuple, Num)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

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

Tuple with multiple copies.

## Example (HDevelop)

```
tuple_repeat (['a', 'b', 'c'], 2, Result)
* Returns ['a', 'b', 'c', 'a', 'b', 'c']
```

## Alternatives

`tuple_gen_const`,
`tuple_concat`

## See also

`tuple_repeat_elem`

## Module

Foundation
