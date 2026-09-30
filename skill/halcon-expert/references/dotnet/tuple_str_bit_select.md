# TupleStrBitSelect (Operator)

## Name

`TupleStrBitSelect` — Select single character or bit from a tuple.

## Signature

`static void HOperatorSet.TupleStrBitSelect(HTuple tuple, HTuple index, out HTuple selected)`

`HTuple HTuple.TupleStrBitSelect(HTuple index)`

## Description

`TupleStrBitSelect` selects a single character or bit from
a tuple *`tuple`* of integer numbers and/or strings.
The input parameter *`index`* determines the character or bit
position to select. *`index`* must contain a single number. If
*`index`* contains a floating point number, this may only
represent an integer value (without fraction). The result tuple
*`selected`* contains a new element for each element of
*`tuple`*. Let *`index`* contain the number “n” then each
element of *`selected`* consists of the “n-th” character
(for strings) or “n-th” bit (for integers) of the corresponding
element of *`tuple`*.

If *`tuple`* is empty, an exception is raised.

### Unicode code points versus bytes

The index reference Unicode code points. One Unicode code point may be
composed of multiple bytes in the UTF-8 string. If the index should
reference the raw bytes of the string, this operator can be switched to byte
mode with `set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleStrBitSelect`,
which can be used in an expression in the following syntax:

[`Selected := Tuple{Index`}](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Input tuple.

**`index`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Position of character or bit to select.

**`selected`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Tuple containing the selected characters and bits.

## Alternatives

`TupleSelect`,
`TupleFirstN`,
`TupleLastN`,
`TupleConcat`,
`TupleStrchr`,
`TupleStrrchr`,
`TupleStrFirstN`,
`TupleStrLastN`,
`TupleSubstr`,
`TupleAnd`,
`TupleOr`,
`TupleXor`,
`TupleNot`

## See also

`TupleRemove`

## Module

Foundation
