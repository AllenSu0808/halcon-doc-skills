# vector_field_length (Operator)

## Name

`vector_field_length` — Compute the length of the vectors of a vector field.

## Signature

`def vector_field_length(vector_field: HObject, mode: str) -> HObject`

## Description

`vector_field_length` compute the length of the vectors of the
vector field *`vector_field`* and returns them in
*`length`*. `vector_field_length` only accepts vector fields of
the semantic type `vector_field_relative`.
The parameter *`mode`* can
be used to specify how the lengths are computed. For *`mode`* =
*"length"*, the Euclidean length of the vectors is computed.
For *`mode`* = *"squared_length"*, the square of the
length of the vectors is computed. This avoids having to compute a
square root internally, which is a costly operation on many
processors, and hence saves runtime on these processors. Note that the
*`vector_field`* must be in relative coordinates as returned by
[`optical_flow_mg`](optical_flow_mg.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.
- Automatically parallelized on tuple level.

## Parameters

**`vector_field`** (input_object)  singlechannelimage(-array) `→` HObject (vector_field)

Input vector field

**`length`** (output_object)  singlechannelimage(-array) `→` HObject (real)

Length of the vectors of the vector field.

**`mode`** (input_control)  string `→` str

Mode for computing the length of the vectors.

Default:
"length"

List of values:
"length", "squared_length"

## Result

If the parameter values are correct, the operator
`vector_field_length` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`optical_flow_mg`

## Possible Successors

`threshold`

## Module

Foundation
