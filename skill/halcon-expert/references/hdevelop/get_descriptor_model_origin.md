# get_descriptor_model_origin (Operator)

## Name

`get_descriptor_model_origin` — Return the origin of a descriptor model.

## Signature

`get_descriptor_model_origin( : : ModelID : Row, Column)`

## Description

The operator `get_descriptor_model_origin` returns the origin
(reference point) of the descriptor model *`ModelID`*.
The origin is specified relative to the center of gravity of the domain
(region) of the image that was used to create the descriptor model
with [`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md), or
[`create_calib_descriptor_model`](create_calib_descriptor_model.md). Hence, an origin of (0,0) means
that the center of gravity of the domain of the model image is used as
the origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  descriptor_model `→`  (handle)

Handle of a descriptor model.

**`Row`** (output_control)  real `→`  (real / integer)

Position of origin in row direction.

**`Column`** (output_control)  real `→`  (real / integer)

Position of origin in column direction.

## Possible Predecessors

`create_uncalib_descriptor_model`,
`read_descriptor_model`

## See also

`set_descriptor_model_origin`,
`create_uncalib_descriptor_model`

## Module

Matching
