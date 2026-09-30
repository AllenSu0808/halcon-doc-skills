# gen_cylinder_object_model_3d (Operator)

## Name

`gen_cylinder_object_model_3d` — Create a 3D object model that represents a cylinder.

## Signature

`gen_cylinder_object_model_3d( : : Pose, Radius, MinExtent, MaxExtent : ObjectModel3D)`

## Description

`gen_cylinder_object_model_3d` creates a cylinder-shaped 3D
primitive, i.e., a 3D object model that represents a cylinder. A
cylinder is described by its center and the direction of its axis in
*`Pose`* and by its radius in *`Radius`*. The pose has the
origin on the rotation axis of the cylinder and is oriented such
that the z-axis is aligned with the main direction of the cylinder.
Additionally, the extensions of the cylinder are
given by *`MinExtent`* and *`MaxExtent`*. *`MinExtent`*
and *`MaxExtent`* represent the z-coordinates of the lowest and
highest points of the cylinder on the rotation axis. The handle of the
3D object model is returned by the parameter *`ObjectModel3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Pose`** (input_control)  pose(-array) `→`  (real / integer)

The pose that describes the position and
orientation of the cylinder.

**`Radius`** (input_control)  number(-array) `→`  (real)

The radius of the cylinder.

**`MinExtent`** (input_control)  number(-array) `→`  (real)

Lowest z-coordinate of the cylinder in the
direction of the rotation axis.

**`MaxExtent`** (input_control)  number(-array) `→`  (real)

Highest z-coordinate of the cylinder in the
direction of the rotation axis.

Restriction:
`MinExtent < MaxExtent`

**`ObjectModel3D`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the resulting 3D object model.

## Result

`gen_cylinder_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Successors

`get_object_model_3d_params`,
`sample_object_model_3d`,
`clear_object_model_3d`

## See also

`gen_sphere_object_model_3d`,
`gen_sphere_object_model_3d_center`,
`gen_plane_object_model_3d`,
`gen_box_object_model_3d`

## Module

3D Metrology
