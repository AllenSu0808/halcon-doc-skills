# AddDeformableSurfaceModelReferencePoint (Operator)

## Name

`AddDeformableSurfaceModelReferencePoint` — Add a reference point to a deformable surface model.

## Signature

`static void HOperatorSet.AddDeformableSurfaceModelReferencePoint(HTuple deformableSurfaceModel, HTuple referencePointX, HTuple referencePointY, HTuple referencePointZ, out HTuple referencePointIndex)`

`HTuple HDeformableSurfaceModel.AddDeformableSurfaceModelReferencePoint(HTuple referencePointX, HTuple referencePointY, HTuple referencePointZ)`

`int HDeformableSurfaceModel.AddDeformableSurfaceModelReferencePoint(double referencePointX, double referencePointY, double referencePointZ)`

## Description

The operator `AddDeformableSurfaceModelReferencePoint` adds
one or more reference points to the deformable surface model passed in
*`deformableSurfaceModel`*.
The 3D coordinates of the reference points is passed in the parameters
*`referencePointX`*, *`referencePointY`* and
*`referencePointZ`*.
The index of the new reference points is returned in
*`referencePointIndex`*.

Reference points are defined in model coordinates, i.e., in the coordinate
frame of the model parameter of [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).
The operators
[`FindDeformableSurfaceModel`](find_deformable_surface_model.md) and
[`RefineDeformableSurfaceModel`](refine_deformable_surface_model.md) return the position of all
added reference points as found in the scene.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- deformableSurfaceModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deformableSurfaceModel`** (input_control, state is modified)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model.

**`referencePointX`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

x-coordinates of a reference point.

**`referencePointY`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

x-coordinates of a reference point.

**`referencePointZ`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

x-coordinates of a reference point.

**`referencePointIndex`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the new reference point.

## Result

`AddDeformableSurfaceModelReferencePoint` returns 2 (
H_MSG_TRUE)
if all
parameters are correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeformableSurfaceModel`,
`ReadDeformableSurfaceModel`

## Possible Successors

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`,
`WriteDeformableSurfaceModel`

## See also

`CreateDeformableSurfaceModel`,
`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`

## Module

3D Metrology
