# tuple_number (Operator)

## Name

`tuple_number` — Convert a tuple (of strings) into a tuple of numbers.

## Signature

`def tuple_number(t: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

`def tuple_number_s(t: MaybeSequence[Union[float, int, str]]) -> Union[float, int, str]`

## Description

`tuple_number` converts the input tuple *`t`* into a tuple of
numbers. If the input tuple contains numbers, they are simply copied into
the output tuple. Strings are converted into the appropriate type of number
(integer or floating point numbers) or are copied as strings if they do not
represent a number. Note that strings starting with 0x are interpreted as
hexadecimal numbers, and strings starting with 0 as octal numbers. For
example, the string '20' is converted to the integer 20, '020' to 16, and
'0x20' to 32.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### Exception: Out of range integers

If the input tuple contains strings with integers that cannot be represented
as Hlong (32-bit signed integer for 32-bit HALCON, 64-bit signed integer
for 64-bit HALCON), an exception is raised.

### String padding

If `tuple_number` converts a string to a number, the same string with
added leading and/or trailing spaces will be converted to the same number.
Example: number('55.6') == 55.6 and number(' 55.6 ') == 55.6

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_number`,
which can be used in an expression in the following syntax:

[`Number := number(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`number`** (output_control)  tuple(-array) `→` Sequence[Union[float, int, str]]

Input tuple as numbers.

## See also

`tuple_is_number`,
`tuple_string`

## Module

Foundation
