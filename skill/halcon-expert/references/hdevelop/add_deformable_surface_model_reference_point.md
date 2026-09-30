# add_deformable_surface_model_reference_point (Operator)

## Name

`add_deformable_surface_model_reference_point` — Add a reference point to a deformable surface model.

## Signature

`add_deformable_surface_model_reference_point( : : DeformableSurfaceModel, ReferencePointX, ReferencePointY, ReferencePointZ : ReferencePointIndex)`

## Description

The operator `add_deformable_surface_model_reference_point` adds
one or more reference points to the deformable surface model passed in
*`DeformableSurfaceModel`*.
The 3D coordinates of the reference points is passed in the parameters
*`ReferencePointX`*, *`ReferencePointY`* and
*`ReferencePointZ`*.
The index of the new reference points is returned in
*`ReferencePointIndex`*.

Reference points are defined in model coordinates, i.e., in the coordinate
frame of the model parameter of [`create_deformable_surface_model`](create_deformable_surface_model.md).
The operators
[`find_deformable_surface_model`](find_deformable_surface_model.md) and
[`refine_deformable_surface_model`](refine_deformable_surface_model.md) return the position of all
added reference points as found in the scene.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- DeformableSurfaceModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DeformableSurfaceModel`** (input_control, state is modified)  deformable_surface_model `→`  (handle)

Handle of the deformable surface model.

**`ReferencePointX`** (input_control)  real(-array) `→`  (real / integer)

x-coordinates of a reference point.

**`ReferencePointY`** (input_control)  real(-array) `→`  (real / integer)

x-coordinates of a reference point.

**`ReferencePointZ`** (input_control)  real(-array) `→`  (real / integer)

x-coordinates of a reference point.

**`ReferencePointIndex`** (output_control)  integer(-array) `→`  (integer)

Index of the new reference point.

## Result

`add_deformable_surface_model_reference_point` returns 2 (
H_MSG_TRUE)
if all
parameters are correct. If necessary, an exception is raised.

## Possible Predecessors

`create_deformable_surface_model`,
`read_deformable_surface_model`

## Possible Successors

`find_deformable_surface_model`,
`refine_deformable_surface_model`,
`write_deformable_surface_model`

## See also

`create_deformable_surface_model`,
`find_deformable_surface_model`,
`refine_deformable_surface_model`

## Module

3D Metrology
