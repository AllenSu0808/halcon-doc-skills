# SetNccModelOrigin (Operator)

## Name

`SetNccModelOrigin` — Set the origin (reference point) of an NCC model.

## Signature

`static void HOperatorSet.SetNccModelOrigin(HTuple modelID, HTuple row, HTuple column)`

`void HNCCModel.SetNccModelOrigin(double row, double column)`

## Description

The operator `SetNccModelOrigin` sets the origin (reference
point) of the NCC model *`modelID`* to a new value. The origin
is specified relative to the center of gravity of the domain
(region) of the image that was used to create the NCC model with
[`CreateNccModel`](create_ncc_model.md). Hence, an origin of (0,0) means that the
center of gravity of the domain of the model image is used as the
origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the origin of the NCC model.

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the origin of the NCC model.

## Result

If the handle of the model is valid, the operator
`SetNccModelOrigin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateNccModel`,
`ReadNccModel`

## Possible Successors

`FindNccModel`,
`GetNccModelOrigin`,
`FindNccModels`

## See also

`AreaCenter`

## Module

Matching
