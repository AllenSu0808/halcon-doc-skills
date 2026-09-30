# gen_plane_object_model_3d (Operator)

## Name

`gen_plane_object_model_3d` — Create a 3D object model that represents a plane.

## Signature

`gen_plane_object_model_3d( : : Pose, XExtent, YExtent : ObjectModel3D)`

## Description

`gen_plane_object_model_3d` creates a planar 3D primitive, i.e.,
a 3D object model that represents a plane. The plane is described by
its center and rotation. The normal vector of the plane is aligned to the
z-axis of the rotated coordinate system. The center and the rotation
is set with the parameter *`Pose`*. Additionally, the plane can
be limited by a polygon, that is defined by points with the coordinates
*`XExtent`* and *`YExtent`*. The handle of the 3D object
model is returned by the parameter *`ObjectModel3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Pose`** (input_control)  pose `→`  (real / integer)

The center and the rotation of the plane.

Number of elements:
Pose == 7

**`XExtent`** (input_control)  point.x(-array) `→`  (real / integer)

x coordinates specifying the extent of the plane.

**`YExtent`** (input_control)  point.y(-array) `→`  (real / integer)

y coordinates specifying the extent of the plane.

Number of elements:
XExtent == YExtent

**`ObjectModel3D`** (output_control)  object_model_3d `→`  (handle)

Handle of the resulting 3D object model.

## Result

`gen_plane_object_model_3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Successors

`get_object_model_3d_params`,
`sample_object_model_3d`,
`clear_object_model_3d`

## See also

`gen_cylinder_object_model_3d`,
`gen_sphere_object_model_3d`,
`gen_sphere_object_model_3d_center`,
`gen_box_object_model_3d`

## Module

3D Metrology
