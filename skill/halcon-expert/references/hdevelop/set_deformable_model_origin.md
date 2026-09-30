# set_deformable_model_origin (Operator)

## Name

`set_deformable_model_origin` — Set the origin (reference point) of a deformable model.

## Signature

`set_deformable_model_origin( : : ModelID, Row, Column : )`

## Description

The operator `set_deformable_model_origin` sets the origin
(reference point) of the deformable model *`ModelID`* to a new
value. The origin is specified relative to the center of gravity of
the domain (region) of the image that was used to create the deformable
model with [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md).
Hence, an origin of (0,0) means that the center of gravity of the domain of
the deformable image is used as the origin. An origin of (-20,-40) means
that the origin lies to the upper left of the center of gravity.
If a deformable model was created by
[`create_planar_calib_deformable_model`](create_planar_calib_deformable_model.md) the 3D pose of the origin
changes by the respective translation. Hence, further calls of
[`find_planar_calib_deformable_model`](find_planar_calib_deformable_model.md) will include the pose offset.
If a deformable model was created by
[`create_planar_calib_deformable_model_xld`](create_planar_calib_deformable_model_xld.md) the 3D pose of the origin
changes directly by the offset. This means that the offsets are interpreted
in world coordinates. In this case, the row coordinate corresponds
to the y world coordinate (from top to down) and the column coordinate
corresponds to the x world coordinate (from left to right).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  deformable_model `→`  (handle)

Handle of the model.

**`Row`** (input_control)  point.y `→`  (real)

Row coordinate of the origin of the deformable model.

**`Column`** (input_control)  point.x `→`  (real)

Column coordinate of the origin of the deformable model.

## Result

If the handle of the model is valid, the operator
`set_deformable_model_origin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`,
`read_deformable_model`

## Possible Successors

`find_planar_uncalib_deformable_model`,
`find_planar_calib_deformable_model`,
`get_deformable_model_origin`

## See also

`area_center`

## Module

Matching
