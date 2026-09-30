# TupleSubstr (Operator)

## Name

`TupleSubstr` — Cut characters from position “n1” through “n2” out of a string tuple.

## Signature

`static void HOperatorSet.TupleSubstr(HTuple stringVal, HTuple position1, HTuple position2, out HTuple substring)`

`HTuple HTuple.TupleSubstr(HTuple position1, HTuple position2)`

## Description

`TupleSubstr` cuts all characters from position “n1” through “n2”
out of each string of the input tuple *`stringVal`* and
returns them as new strings in the output tuple *`substring`*. The
positions “n1” and “n2” are determined by the second and third input
tuples *`position1`* and *`position2`*. Their
length has to be equal. If *`position1`* and *`position2`* only
contain one element, this element defines for all strings of
*`stringVal`* “n1” and “n2”, respectively . If
*`stringVal`*, *`position1`* and *`position2`* have got the
same number of elements, the first elements of *`position1`* and
*`position2`* determine the start and end position for the
first string of *`stringVal`*. The second elements of *`position1`*
and *`position2`* do so for the second string of *`stringVal`*
and so on. If *`position1`* and *`position2`*
contain more than one element and *`stringVal`* contains only one string,
`TupleSubstr` cuts more than one substring out of this string.
The elements of *`position1`* and *`position2`* then determine
the start and end positions for
these substrings. If all input tuples contain more than one element but
differ in the number of elements, `TupleSubstr` returns an error.

If *`stringVal`* is an empty tuple, the operator returns an empty tuple.
If *`stringVal`* is not empty and *`position1`* and/or
*`position2`* are empty tuples, an exception is raised.

### Unicode code points versus bytes

The positions reference Unicode code points. One Unicode code point may be
composed of multiple bytes in the UTF-8 string. If the positions should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSubstr`,
which can be used in an expression in the following syntax:

[`Substring := String{Position1:Position2`}](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stringVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with string(s) to examine.

**`position1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple with start position(s) “n1”.

**`position2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Input tuple with end position(s) “n2”.

**`substring`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Characters of the string(s) from position “n1” to “n2”.

## Alternatives

`TupleStrFirstN`,
`TupleStrLastN`,
`TupleStrstr`,
`TupleStrrstr`,
`TupleStrlen`,
`TupleStrchr`,
`TupleStrrchr`,
`TupleSplit`,
`TupleEnvironment`

## Module

Foundation
