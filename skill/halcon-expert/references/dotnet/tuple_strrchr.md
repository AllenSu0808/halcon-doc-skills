# TupleStrrchr (Operator)

## Name

`TupleStrrchr` — Backward search for characters within a string tuple.

## Signature

`static void HOperatorSet.TupleStrrchr(HTuple stringVal, HTuple toFind, out HTuple position)`

`HTuple HTuple.TupleStrrchr(HTuple toFind)`

## Description

`TupleStrrchr` searches within the strings of the input tuple
*`stringVal`* for the characters of the input tuple *`toFind`*. Both
input tuples may only consist of strings. Otherwise `TupleStrrchr`
returns an error. In any case backward search is used, i.e., every string is
examined from its last to its first character. If the elements of
*`toFind`* contain more than one character, only the first character of
each element is considered for searching. If *`stringVal`* contains only
one string, all the characters defined in *`toFind`* are searched in
this string. Thus, the output tuple consists of as many elements as
*`toFind`*. Whenever a searched character has been found, the position
of its first occurrence gets stored in the output tuple *`position`* . If
a character can not be found, -1 will be returned instead of its position
(remark: the position starts at 0 for the first character of a string). If
both input tuples show the same number of elements, the search is done
elementwise. I.e., the first character of the first element of
*`toFind`* is searched within the first string of *`stringVal`*, the
first character of the second element of *`toFind`* is searched within
the second string of *`stringVal`* and so on. The results of the
elementwise searches are returned with *`position`* that contains as
many elements as *`stringVal`* and *`toFind`*. If *`toFind`* only
contains one string, its first character is searched within all strings of
*`stringVal`*. Thus, in this case *`position`* consists of as many
elements as *`stringVal`*. If both input tuples contain more than one
element and the number of elements differs for the input tuples,
`TupleStrrchr` returns an error.

If either or both of the input tuples are empty, the operator returns an
empty tuple.

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

HDevelop provides an in-line operation for `TupleStrrchr`,
which can be used in an expression in the following syntax:

[`Position := strrchr(String, ToFind)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stringVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with string(s) to examine.

**`toFind`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with character(s) to search.

**`position`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Position of searched character(s) within the string(s).

## Alternatives

`TupleStrchr`,
`TupleStrstr`,
`TupleStrrstr`,
`TupleStrlen`,
`TupleSubstr`,
`TupleStrFirstN`,
`TupleStrLastN`,
`TupleSplit`,
`TupleEnvironment`

## Module

Foundation
