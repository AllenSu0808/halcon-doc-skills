# SetShapeModelOrigin (Operator)

## Name

`SetShapeModelOrigin` — Set the origin (reference point) of a shape model.

## Signature

`static void HOperatorSet.SetShapeModelOrigin(HTuple modelID, HTuple row, HTuple column)`

`void HShapeModel.SetShapeModelOrigin(double row, double column)`

## Description

The operator `SetShapeModelOrigin` sets the origin
(reference point) of the shape model *`modelID`* to a new
value. The origin is specified relative to the center of gravity of
the domain (region) of the image that was used to create the shape
model with [`CreateShapeModel`](create_shape_model.md),
[`CreateScaledShapeModel`](create_scaled_shape_model.md), or
[`CreateAnisoShapeModel`](create_aniso_shape_model.md). Hence, an origin of (0,0) means
that the center of gravity of the domain of the model image is used
as the origin. An origin of (-20,-40) means that the origin lies to
the upper left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the origin of the shape model.

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the origin of the shape model.

## Result

If the handle of the model is valid, the operator
`SetShapeModelOrigin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateGenericShapeModel`

## Possible Successors

`TrainGenericShapeModel`

## See also

`AreaCenter`

## Module

Matching
