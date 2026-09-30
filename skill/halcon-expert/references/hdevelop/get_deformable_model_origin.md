# get_deformable_model_origin (Operator)

## Name

`get_deformable_model_origin` — Return the origin (reference point) of a deformable model.

## Signature

`get_deformable_model_origin( : : ModelID : Row, Column)`

## Description

The operator `get_deformable_model_origin` returns the origin
(reference point) of the deformable model *`ModelID`*.
The origin is specified relative to the center of gravity of the domain
(region) of the image that was used to create the deformable model with
[`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md) or
[`create_planar_calib_deformable_model`](create_planar_calib_deformable_model.md). Hence, an origin of (0,0)
means that the center of gravity of the domain of the model image is used as
the origin. An origin of (-20,-40) means that the origin lies to the upper
left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  deformable_model `→`  (handle)

Handle of the model.

**`Row`** (output_control)  point.y `→`  (real)

Row coordinate of the origin of the deformable model.

**`Column`** (output_control)  point.x `→`  (real)

Column coordinate of the origin of the deformable model.

## Result

If the handle of the model is valid, the operator
`get_deformable_model_origin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_planar_uncalib_deformable_model`,
`read_deformable_model`,
`set_deformable_model_origin`

## Possible Successors

`find_planar_uncalib_deformable_model`

## See also

`area_center`

## Module

Matching
