# get_ncc_model_origin (Operator)

## Name

`get_ncc_model_origin` — Return the origin (reference point) of an NCC model.

## Signature

`get_ncc_model_origin( : : ModelID : Row, Column)`

## Description

The operator `get_ncc_model_origin` returns the origin
(reference point) of the NCC model *`ModelID`*. The origin is
specified relative to the center of gravity of the domain (region)
of the image that was used to create the NCC model with
[`create_ncc_model`](create_ncc_model.md). Hence, an origin of (0,0) means that the
center of gravity of the domain of the model image is used as the
origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  ncc_model `→`  (handle)

Handle of the model.

**`Row`** (output_control)  point.y `→`  (real)

Row coordinate of the origin of the NCC model.

**`Column`** (output_control)  point.x `→`  (real)

Column coordinate of the origin of the NCC model.

## Result

If the handle of the model is valid, the operator
`get_ncc_model_origin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_ncc_model`,
`read_ncc_model`,
`set_ncc_model_origin`

## Possible Successors

`find_ncc_model`

## See also

`area_center`

## Module

Matching
