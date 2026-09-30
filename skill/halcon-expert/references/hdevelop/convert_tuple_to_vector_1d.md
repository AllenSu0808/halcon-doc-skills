# convert_tuple_to_vector_1d (Operator)

## Name

`convert_tuple_to_vector_1d` — Distribute the elements of a tuple to a vector.

## Signature

`convert_tuple_to_vector_1d( : : InputTuple, SubTupleLength : ResultVector)`

## Description

`convert_tuple_to_vector_1d` transforms a tuple into
a vector variable. The input tuple *`InputTuple`* is split into
sub-tuples each comprising of *`SubTupleLength`* elements. The
sub-tuples are stored in the output vector *`ResultVector`*.

## Parameters

**`InputTuple`** (input_control)  number(-array) `→`  (real / integer / string)

Input tuple.

**`SubTupleLength`** (input_control)  number `→`  (integer)

Desired length of the resulting tuples in the output
vector.

Default:
1

**`ResultVector`** (output_control)  number-vector{1} `→`  (real / integer / string)

Output vector.

## Result

If the values of the specified parameters are correct,
`convert_tuple_to_vector_1d` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## See also

`convert_vector_to_tuple`

## Module

Foundation
