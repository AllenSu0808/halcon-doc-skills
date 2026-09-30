# tuple_gen_sequence (Operator)

## Name

`tuple_gen_sequence` — Generate a tuple with a sequence of equidistant values.

## Signature

`tuple_gen_sequence( : : Start, End, Step : Sequence)`

## Description

`tuple_gen_sequence` generates a new tuple *`Sequence`* with
a sequence of equidistant values:

[Start, Start + Step, Start + 2*Step, ... End]

*`Step`* must not be zero and the sign of
(*`End`* - *`Start`*) must be equal to the sign of *`Step`*.
The last entry of *`Sequence`* may actually be less than *`End`*,
if (*`End`* - *`Start`*) is not divisible by *`Step`* without
remainder.

### Exception: Empty input tuples

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_gen_sequence`,
which can be used in an expression in the following syntax:

[`Sequence := [Start:Step:End]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

An alternative syntax is
[`Sequence := [Start:End]`,](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)
where *`Step`* defaults to *1*.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Start`** (input_control)  number `→`  (integer / real)

Start value of the tuple.

**`End`** (input_control)  number `→`  (integer / real)

Maximum value for the last entry.

**`Step`** (input_control)  number `→`  (integer / real)

Increment value.

**`Sequence`** (output_control)  number(-array) `→`  (integer / real)

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
