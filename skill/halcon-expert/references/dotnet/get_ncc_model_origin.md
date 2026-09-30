# GetNccModelOrigin (Operator)

## Name

`GetNccModelOrigin` — Return the origin (reference point) of an NCC model.

## Signature

`static void HOperatorSet.GetNccModelOrigin(HTuple modelID, out HTuple row, out HTuple column)`

`void HNCCModel.GetNccModelOrigin(out double row, out double column)`

## Description

The operator `GetNccModelOrigin` returns the origin
(reference point) of the NCC model *`modelID`*. The origin is
specified relative to the center of gravity of the domain (region)
of the image that was used to create the NCC model with
[`CreateNccModel`](create_ncc_model.md). Hence, an origin of (0,0) means that the
center of gravity of the domain of the model image is used as the
origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`row`** (output_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the origin of the NCC model.

**`column`** (output_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the origin of the NCC model.

## Result

If the handle of the model is valid, the operator
`GetNccModelOrigin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateNccModel`,
`ReadNccModel`,
`SetNccModelOrigin`

## Possible Successors

`FindNccModel`

## See also

`AreaCenter`

## Module

Matching
