# TupleNumber (Operator)

## Name

`TupleNumber` — Convert a tuple (of strings) into a tuple of numbers.

## Signature

`static void HOperatorSet.TupleNumber(HTuple t, out HTuple number)`

`HTuple HTuple.TupleNumber()`

## Description

`TupleNumber` converts the input tuple *`t`* into a tuple of
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

If `TupleNumber` converts a string to a number, the same string with
added leading and/or trailing spaces will be converted to the same number.
Example: number('55.6') == 55.6 and number(' 55.6 ') == 55.6

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleNumber`,
which can be used in an expression in the following syntax:

[`Number := number(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Input tuple.

**`number`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Input tuple as numbers.

## See also

`TupleIsNumber`,
`TupleString`

## Module

Foundation
