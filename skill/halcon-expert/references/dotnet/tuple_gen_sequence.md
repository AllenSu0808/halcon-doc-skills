# TupleGenSequence (Operator)

## Name

`TupleGenSequence` — Generate a tuple with a sequence of equidistant values.

## Signature

`static void HOperatorSet.TupleGenSequence(HTuple start, HTuple end, HTuple step, out HTuple sequence)`

`static HTuple HTuple.TupleGenSequence(HTuple start, HTuple end, HTuple step)`

## Description

`TupleGenSequence` generates a new tuple *`sequence`* with
a sequence of equidistant values:

[Start, Start + Step, Start + 2*Step, ... End]

*`step`* must not be zero and the sign of
(*`end`* - *`start`*) must be equal to the sign of *`step`*.
The last entry of *`sequence`* may actually be less than *`end`*,
if (*`end`* - *`start`*) is not divisible by *`step`* without
remainder.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleGenSequence`,
which can be used in an expression in the following syntax:

[`Sequence := [Start:Step:End]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

An alternative syntax is
[`Sequence := [Start:End]`,](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)
where *`step`* defaults to *1*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`start`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Start value of the tuple.

**`end`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Maximum value for the last entry.

**`step`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Increment value.

**`sequence`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

The resulting sequence.

## Alternatives

`TupleStrBitSelect`,
`TupleSelect`,
`TupleStrFirstN`,
`TupleStrLastN`,
`TupleConcat`,
`TupleInsert`,
`TupleReplace`,
`TupleGenConst`

## See also

`TupleRand`

## Module

Foundation
