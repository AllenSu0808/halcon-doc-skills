# tuple_gen_sequence (Operator)

## Name

`tuple_gen_sequence` — Generate a tuple with a sequence of equidistant values.

## Signature

`def tuple_gen_sequence(start: Union[float, int], end: Union[float, int], step: Union[float, int]) -> Sequence[Union[float, int]]`

`def tuple_gen_sequence_s(start: Union[float, int], end: Union[float, int], step: Union[float, int]) -> Union[float, int]`

## Description

`tuple_gen_sequence` generates a new tuple *`sequence`* with
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

HDevelop provides an in-line operation for `tuple_gen_sequence`,
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

**`start`** (input_control)  number `→` Union[float, int]

Start value of the tuple.

**`end`** (input_control)  number `→` Union[float, int]

Maximum value for the last entry.

**`step`** (input_control)  number `→` Union[float, int]

Increment value.

**`sequence`** (output_control)  number(-array) `→` Sequence[Union[float, int]]

The resulting sequence.

## Alternatives

`tuple_str_bit_select`,
`tuple_select`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_concat`,
`tuple_insert`,
`tuple_replace`,
`tuple_gen_const`

## See also

`tuple_rand`

## Module

Foundation
