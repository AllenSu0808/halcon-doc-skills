# TupleOrds (Operator)

## Name

`TupleOrds` — Convert a tuple of strings into a tuple of integer numbers.

## Signature

`static void HOperatorSet.TupleOrds(HTuple t, out HTuple ords)`

`HTuple HTuple.TupleOrds()`

## Description

`TupleOrds` converts the input tuple *`t`*, which may
only contain strings and integer numbers, into a tuple of integer
numbers.
When the encoding used in the HALCON library is UTF-8 (see
`set_system('filename_encoding', 'utf8')`) and the string operators
are set to work by code points (see
`set_system('tuple_string_operator_mode', 'codepoint')`), which is the
default for both, the operator returns for the input strings the appropriate
Unicode character codes.
When the HALCON library encoding is set to *"locale"* or the string
operator mode is *"byte"*, the operator returns the ANSI code for
every byte of the input string.
In that mode, the result may depend on the currently used code page for
strings that contain non-ASCII characters.
See also [Tuple / String Operations](toc_tuple_stringoperations.md) for a more detailed description
of the different modes and further encoding issues.

The character codes of the individual strings are written to the output
according to their order within the string and within the tuple.
Integer numbers are simply copied to an appropriate position in the
output tuple.
This operator can be used to prepare outputs with [`WriteSerial`](write_serial.md).
In particular, a byte with value 0 can be written by inserting the integer
number 0 into *`t`*.

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleOrds`,
which can be used in an expression in the following syntax:

[`Ords := ords(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Input tuple with strings.

**`ords`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Output tuple with the Unicode character codes or ANSI codes of
the input string.

## Example (HDevelop)

```
tuple_ords (['String 1', 0, 'String 2', 0], Data)
write_serial (SerialHandle, Data)
```

## Alternatives

`TupleOrd`

## See also

`TupleChr`,
`TupleChrt`,
`WriteSerial`

## Module

Foundation
