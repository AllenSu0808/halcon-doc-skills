# TupleChrt (Operator)

## Name

`TupleChrt` — Convert a tuple of integer numbers into strings.

## Signature

`static void HOperatorSet.TupleChrt(HTuple t, out HTuple chrt)`

`HTuple HTuple.TupleChrt()`

## Description

`TupleChrt` converts the input tuple *`t`*, consisting of integer
numbers, into a tuple of strings and integer numbers (where only the number 0
is passed as number to the output).
All other numbers are converted to characters that are concatenated to one
string up to the next 0 in the input tuple.
When the encoding used in the HALCON library is UTF-8 (see
`set_system('filename_encoding', 'utf8')`) and the string operators
are set to work by code points (see
`set_system('tuple_string_operator_mode', 'codepoint')`), which is the
default for both, the operator interprets the input numbers as Unicode
character codes and transforms them to the appropriate UTF-8 representations
of the characters.
When the HALCON library encoding is set to *"locale"* or the string
operator mode is *"byte"*, the operator accepts only numbers between
0 and 256.
In that case they are interpreted as ANSI codes from which the output string
has to be built byte by byte.
In that mode it is not checked whether the byte sequences will build valid
characters according to the current string encoding.
See also [Tuple / String Operations](toc_tuple_stringoperations.md) for a more detailed description
of the different modes and further encoding issues.

The operator tries to pack as many input numbers into one string as possible.
If the number 0 occurs in the input tuple *`t`*, the current string is
terminated and the number 0 is added to the output tuple.
If in the input tuple more numbers follow, a new string is started.
This operator can be used to convert data read with [`ReadSerial`](read_serial.md) into
strings.
This approach allows also to read bytes with the value 0.

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleChrt`,
which can be used in an expression in the following syntax:

[`Chrt := chrt(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Input tuple with integer numbers.

Restriction:
`0 <= T`

**`chrt`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Output tuple with strings that are separated by the number 0.

## Example (HDevelop)

```
read_serial (SerialHandle, 100, Data)
tuple_chrt (Data, Strings)
```

## Alternatives

`TupleChr`

## See also

`TupleOrd`,
`TupleOrds`,
`ReadSerial`

## Module

Foundation
