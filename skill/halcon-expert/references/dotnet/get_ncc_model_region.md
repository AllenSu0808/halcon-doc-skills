# GetNccModelRegion (Operator)

## Name

`GetNccModelRegion` — Return the region used to create an NCC model.

## Signature

`static void HOperatorSet.GetNccModelRegion(out HObject modelRegion, HTuple modelID)`

`HRegion HNCCModel.GetNccModelRegion()`

## Description

The operator `GetNccModelRegion` returns the
region used to create the NCC model *`modelID`* in
*`modelRegion`*. This region can be used, for example, to
visualize the found instances of the model in an image. It should
be noted that the position of *`modelRegion`* is normalized
such that the reference point of the model (see [`SetNccModelOrigin`](set_ncc_model_origin.md))
lies at the pixel position (0,0).
Hence, the region simply needs to be translated to the found
position in the image (and possibly rotated around this
point).
`GetNccModelRegion` ignores the value of the system
parameter *"clip_region"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelRegion`** (output_object)  region `→` [HRegion](HRegion.md)

Model region of the NCC model.

**`modelID`** (input_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the handle of the NCC model is valid, the operator
`GetNccModelRegion` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateNccModel`

## Module

Matching
