# TupleStrLastN (Operator)

## Name

`TupleStrLastN` — Cut all characters starting at position “n” out of a string tuple.

## Signature

`static void HOperatorSet.TupleStrLastN(HTuple stringVal, HTuple position, out HTuple substring)`

`HTuple HTuple.TupleStrLastN(HTuple position)`

## Description

`TupleStrLastN` cuts all characters from position “n” to the end
of the string out of each string of the input tuple *`stringVal`* and
returns them as new strings in the output tuple *`substring`*. The
position “n” is determined by the second input tuple *`position`*. If
*`position`* only contains one element, this element contains “n”. If
*`stringVal`* and *`position`* have got the same number of elements,
the first element of *`position`* determines the start position for the
first string of *`stringVal`*, the second element of *`position`* does
so for the second string of *`stringVal`* and so on. If *`position`*
contains more than one element and *`stringVal`* contains only one string,
`TupleStrLastN` cuts more than one substrings out of this string.
The elements of *`position`* then determine the start positions for
these substrings. If both input tuples contain more than one element but
differ in the number of elements, `TupleStrLastN` returns an error.

If both input tuples are empty, the operator returns an empty tuple.
Similarly, if *`stringVal`* is empty and *`position`* is
not, the operator returns an empty tuple. In contrast, if *`position`*
is empty and *`stringVal`* is not, an exception is raised.

### Unicode code points versus bytes

The position references Unicode code points. One Unicode code point may be
composed of multiple bytes in the UTF-8 string. If the position should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleStrLastN`,
which can be used in an expression in the following syntax:

[`Substring := str_lastn(String, Position)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stringVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with string(s) to examine.

**`position`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple with position(s) “n”.

**`substring`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

The last characters of the string(s) starting at position “n”.

## Alternatives

`TupleStrFirstN`,
`TupleSubstr`,
`TupleStrstr`,
`TupleStrrstr`,
`TupleStrlen`,
`TupleStrchr`,
`TupleStrrchr`,
`TupleSplit`,
`TupleEnvironment`

## Module

Foundation
