# TupleOrd (Operator)

## Name

`TupleOrd` — Convert a tuple of strings of length 1 into a tuple of integer numbers.

## Signature

`static void HOperatorSet.TupleOrd(HTuple t, out HTuple ord)`

`HTuple HTuple.TupleOrd()`

## Description

`TupleOrd` converts the input tuple *`t`*, which may only contain
strings of length 1, into a tuple of integer numbers.
When the encoding used in the HALCON library is UTF-8 (see
`set_system('filename_encoding', 'utf8')`) and the string operators
are set to work by code points (see
`set_system('tuple_string_operator_mode', 'codepoint')`), which is the
default for both, the operator accepts the UTF-8 representation of a
Unicode character (code point) and returns the appropriate Unicode character
code.
When the HALCON library encoding is set to *"locale"* or the string
operator mode is *"byte"*, the operator accepts only a single byte for
each input string.
In that case the operator `TupleOrd` returns the ANSI code of the
input byte as integer number between 0 and 256.
See also [Tuple / String Operations](toc_tuple_stringoperations.md) for a more detailed description
of the different modes and further encoding issues.

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleOrd`,
which can be used in an expression in the following syntax:

[`Ord := ord(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_misc_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with strings of length 1.

**`ord`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Output tuple with Unicode character codes or ANSI codes of the
characters passed in the input tuple.

## Alternatives

`TupleOrds`

## See also

`TupleChr`,
`TupleChrt`

## Module

Foundation
