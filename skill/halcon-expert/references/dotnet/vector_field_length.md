# VectorFieldLength (Operator)

## Name

`VectorFieldLength` — Compute the length of the vectors of a vector field.

## Signature

`static void HOperatorSet.VectorFieldLength(HObject vectorField, out HObject length, HTuple mode)`

`HImage HImage.VectorFieldLength(string mode)`

## Description

`VectorFieldLength` compute the length of the vectors of the
vector field *`vectorField`* and returns them in
*`length`*. `VectorFieldLength` only accepts vector fields of
the semantic type `vector_field_relative`.
The parameter *`mode`* can
be used to specify how the lengths are computed. For *`mode`* =
*"length"*, the Euclidean length of the vectors is computed.
For *`mode`* = *"squared_length"*, the square of the
length of the vectors is computed. This avoids having to compute a
square root internally, which is a costly operation on many
processors, and hence saves runtime on these processors. Note that the
*`vectorField`* must be in relative coordinates as returned by
[`OpticalFlowMg`](optical_flow_mg.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.
- Automatically parallelized on tuple level.

## Parameters

**`vectorField`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (vector_field)

Input vector field

**`length`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Length of the vectors of the vector field.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode for computing the length of the vectors.

Default:
"length"

List of values:
"length", "squared_length"

## Result

If the parameter values are correct, the operator
`VectorFieldLength` returns the value 2 (
H_MSG_TRUE)
. If the input is
empty (no input images are available) the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`OpticalFlowMg`

## Possible Successors

`Threshold`

## Module

Foundation
