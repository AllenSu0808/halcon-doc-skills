# GetDeformableModelOrigin (Operator)

## Name

`GetDeformableModelOrigin` — Return the origin (reference point) of a deformable model.

## Signature

`static void HOperatorSet.GetDeformableModelOrigin(HTuple modelID, out HTuple row, out HTuple column)`

`void HDeformableModel.GetDeformableModelOrigin(out double row, out double column)`

## Description

The operator `GetDeformableModelOrigin` returns the origin
(reference point) of the deformable model *`modelID`*.
The origin is specified relative to the center of gravity of the domain
(region) of the image that was used to create the deformable model with
[`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md) or
[`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md). Hence, an origin of (0,0)
means that the center of gravity of the domain of the model image is used as
the origin. An origin of (-20,-40) means that the origin lies to the upper
left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`row`** (output_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the origin of the deformable model.

**`column`** (output_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the origin of the deformable model.

## Result

If the handle of the model is valid, the operator
`GetDeformableModelOrigin` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreatePlanarUncalibDeformableModel`,
`ReadDeformableModel`,
`SetDeformableModelOrigin`

## Possible Successors

`FindPlanarUncalibDeformableModel`

## See also

`AreaCenter`

## Module

Matching
