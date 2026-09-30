# gen_box_object_model_3d (Operator)

## Name

`gen_box_object_model_3d` — Create a 3D object model that represents a box.

## Signature

`gen_box_object_model_3d( : : Pose, LengthX, LengthY, LengthZ : ObjectModel3D)`

## Description

`gen_box_object_model_3d` creates a box-shaped 3D primitive, i.e.,
a 3D object model that represents a box. The box is specified by a
*`Pose`* and the side lengths *`LengthX`*, *`LengthY`*, and
*`LengthZ`* along the respective axis of the pose. The handle of
the resulting 3D object model is returned by parameter
*`ObjectModel3D`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

The pose that describes the position and
orientation of the box. The pose has its
origin in the center of the box.

**`LengthX`** (input_control)  number(-array) `→`  (real)

The length of the box along the x-axis.

**`LengthY`** (input_control)  number(-array) `→`  (real)

The length of the box along the y-axis.

Number of elements:
LengthY == LengthX

**`LengthZ`** (input_control)  number(-array) `→`  (real)

The length of the box along the z-axis.

Number of elements:
LengthZ == LengthX

**`ObjectModel3D`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the resulting 3D object model.

## Result

`gen_box_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`smallest_bounding_box_object_model_3d`

## Possible Successors

`get_object_model_3d_params`,
`sample_object_model_3d`,
`clear_object_model_3d`

## See also

`gen_cylinder_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_sphere_object_model_3d_center`,
`gen_plane_object_model_3d`

## Module

3D Metrology
