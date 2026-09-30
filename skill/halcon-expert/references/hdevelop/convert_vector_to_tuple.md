# convert_vector_to_tuple (Operator)

## Name

`convert_vector_to_tuple` — Concatenate the elements of a vector to a single tuple.

## Signature

`convert_vector_to_tuple( : : InputVector : ResultTuple)`

## Description

`convert_vector_to_tuple` transforms a vector into
a tuple. The elements of the input vector *`InputVector`* get
concatenated and stored in the output tuple *`ResultTuple`*. If
*`InputVector`* has a dimension of 2 or greater its elements are
collected in a depth-first search. E.g., the input vector
*'{{{1},{2}},{{3},{4}}}'* will be turned into the result tuple
*[1,2,3,4]*.

## Parameters

**`InputVector`** (input_control)  number-vector `→`  (real / integer / string)

Input vector.

**`ResultTuple`** (output_control)  real(-array) `→`  (real / integer / string)

Output tuple.

## Result

If the values of the specified parameters are correct,
`convert_vector_to_tuple` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## See also

`convert_tuple_to_vector_1d`

## Module

Foundation
